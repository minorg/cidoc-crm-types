import logging
from typing import Tuple

from rdflib import BNode, Graph, OWL, RDF, RDFS, SKOS, URIRef

from cidoc_crm_types_generator.ecrm_owl import EcrmOwl
from cidoc_crm_types_generator.entity_class import EntityClass
from cidoc_crm_types_generator.property import Property
from cidoc_crm_types_generator.property_restriction import PropertyRestriction
from cidoc_crm_types_generator.property_type import PropertyType


class EcrmOwlParser:
    """
    Parser for the Erlangen CRM OWL (http://erlangen-crm.org/)
    """

    def __init__(self):
        self.__logger = logging.getLogger(self.__class__.__name__)

    def __check_exhaustiveness(
        self,
        *,
        entity_classes: Tuple[EntityClass, ...],
        graph: Graph,
        properties: Tuple[Property, ...],
    ):
        covered_subject_uris = {entity_class.uri for entity_class in entity_classes}
        covered_subject_uris.add(
            URIRef("http://erlangen-crm.org/current/")
        )  # Ignore the owl:Ontology
        for property_ in properties:
            covered_subject_uris.add(property_.uri)

        exhaustive = True
        for subject_uri in graph.subjects():
            if isinstance(subject_uri, BNode):
                continue
            if subject_uri not in covered_subject_uris:
                self.__logger.error("unaccounted-for subject URI: %s", subject_uri)
                exhaustive = False
        if not exhaustive:
            raise ValueError("coverage is not exhaustive")

    def __check_references(
        self,
        *,
        entity_classes: Tuple[EntityClass, ...],
        properties: Tuple[Property, ...],
    ):
        entity_classes_by_uri = {
            entity_class.uri: entity_class for entity_class in entity_classes
        }
        assert len(entity_classes_by_uri) == len(entity_classes)

        properties_by_uri = {property.uri: property for property in properties}
        assert len(properties_by_uri) == len(properties)

        dangling_reference = False

        for entity_class in entity_classes:
            if (
                entity_class.disjoint_with is not None
                and entity_class.disjoint_with not in entity_classes_by_uri
            ):
                self.__logger.error(
                    "entity class %s disjoint with refers to missing %s",
                    entity_class.uri,
                    entity_class.disjoint_with,
                )
                dangling_reference = True

            for property_restriction in entity_class.property_restrictions:
                if property_restriction.on_property not in properties_by_uri:
                    self.__logger.error(
                        "entity class %s has property restriction on missing property %s",
                        entity_class.uri,
                        property_restriction.on_property,
                    )
                    dangling_reference = True

            for sub_class_of in entity_class.sub_class_of:
                if sub_class_of not in entity_classes_by_uri:
                    self.__logger.error(
                        "entity class %s subClassOf refers to missing %s",
                        entity_class.uri,
                        sub_class_of,
                    )
                    dangling_reference = True

        for property_ in properties:
            if (
                property_.domain is not None
                and property_.domain not in entity_classes_by_uri
            ):
                self.__logger.error(
                    "property %s refers to missing domain %s",
                    property_.uri,
                    property_.domain,
                )
                dangling_reference = True

            if (
                property_.inverse_of is not None
                and property_.inverse_of not in properties_by_uri
            ):
                self.__logger.error(
                    "property %s inverse_of refers to missing %s",
                    property_.uri,
                    property_.inverse_of,
                )
                dangling_reference = True

            if (
                property_.range is not None
                and property_.range not in entity_classes_by_uri
            ):
                self.__logger.error(
                    "property %s refers to missing range %s",
                    property_.uri,
                    property_.range,
                )
                dangling_reference = True

            for sub_property_of in property_.sub_property_of:
                if sub_property_of not in properties_by_uri:
                    self.__logger.error(
                        "property %s subPropertyOf refers to missing %s",
                        property_.uri,
                        sub_property_of,
                    )
                    dangling_reference = True

        if dangling_reference:
            raise ValueError("dangling reference")

    def parse(self, graph: Graph) -> EcrmOwl:
        entity_classes = self.__parse_entity_classes(graph)
        properties = self.__parse_properties(graph)
        self.__check_exhaustiveness(
            entity_classes=entity_classes, graph=graph, properties=properties
        )
        self.__check_references(entity_classes=entity_classes, properties=properties)
        return EcrmOwl(entity_classes=entity_classes, properties=properties)

    def __parse_entity_class(self, *, entity_class_uri: URIRef, graph: Graph):
        comment = None
        disjoint_with = None
        label = None
        notation = None
        property_restrictions = []
        sub_class_of = []
        for entity_class_predicate, entity_class_object in graph.predicate_objects(
            entity_class_uri
        ):
            if entity_class_predicate == OWL.disjointWith:
                assert disjoint_with is None, entity_class_uri
                disjoint_with = entity_class_object
                assert isinstance(disjoint_with, URIRef)
            elif entity_class_predicate == RDF.type:
                continue
            elif entity_class_predicate == RDFS.comment:
                assert comment is None, entity_class_uri
                comment = entity_class_object.value
                assert isinstance(comment, str)
            elif entity_class_predicate == RDFS.label:
                assert label is None, entity_class_uri
                label = entity_class_object.value
                assert isinstance(label, str)
            elif entity_class_predicate == RDFS.subClassOf:
                if isinstance(entity_class_object, URIRef):
                    if entity_class_object == OWL.Thing:
                        continue
                    sub_class_of.append(entity_class_object)
                elif isinstance(entity_class_object, BNode):
                    property_restrictions.append(
                        self.__parse_property_restriction(
                            graph=graph, property_restriction_uri=entity_class_object,
                        )
                    )
                else:
                    raise NotImplementedError
            elif entity_class_predicate == SKOS.notation:
                assert notation is None, entity_class_uri
                notation = entity_class_object.value
            else:
                self.__logger.warning(
                    "unhandled entity class (%s) entity_class_predicate: %s, %s (%s)",
                    entity_class_uri,
                    entity_class_predicate,
                    entity_class_object,
                    type(entity_class_object),
                )
        return EntityClass(
            comment=comment,
            disjoint_with=disjoint_with,
            label=label,
            notation=notation,
            property_restrictions=tuple(property_restrictions),
            sub_class_of=tuple(sub_class_of),
            uri=entity_class_uri,
        )

    def __parse_entity_classes(self, graph: Graph) -> Tuple[EntityClass, ...]:
        return tuple(
            self.__parse_entity_class(graph=graph, entity_class_uri=entity_class_uri)
            for entity_class_uri in graph.subjects(RDF.type, OWL.Class)
        )

    def __parse_properties(self, graph: Graph) -> Tuple[Property, ...]:
        properties_by_uri = {}
        for property_rdf_type in (
            OWL.DatatypeProperty,
            OWL.FunctionalProperty,
            OWL.InverseFunctionalProperty,
            OWL.ObjectProperty,
        ):
            for property_uri in graph.subjects(RDF.type, property_rdf_type):
                property_ = self.__parse_property(
                    graph=graph, property_uri=property_uri,
                )
                existing_property = properties_by_uri.get(property_)
                if existing_property is None:
                    properties_by_uri[property_.uri] = property_
                else:
                    assert existing_property == property_, property_.uri
        return tuple(properties_by_uri.values())

    def __parse_property(self, *, graph: Graph, property_uri: URIRef) -> Property:
        comment = None
        domain = None
        inverse_of = None
        label = None
        notation = None
        property_types = []
        range = None
        sub_property_of = []
        for property_predicate, property_object in graph.predicate_objects(
            property_uri
        ):
            if property_predicate == OWL.inverseOf:
                assert inverse_of is None
                inverse_of = property_object
                assert isinstance(inverse_of, URIRef)
            elif property_predicate == RDF.type:
                if property_object == OWL.DatatypeProperty:
                    property_types.append(PropertyType.DATATYPE)
                elif property_object == OWL.FunctionalProperty:
                    property_types.append(PropertyType.FUNCTIONAL)
                elif property_object == OWL.InverseFunctionalProperty:
                    property_types.append(PropertyType.INVERSE_FUNCTIONAL)
                elif property_object == OWL.ObjectProperty:
                    property_types.append(PropertyType.OBJECT)
                elif property_object == OWL.SymmetricProperty:
                    property_types.append(PropertyType.SYMMETRIC)
                elif property_object == OWL.TransitiveProperty:
                    property_types.append(PropertyType.TRANSITIVE)
                else:
                    raise NotImplementedError(property_object)
            elif property_predicate == RDFS.comment:
                assert comment is None, property_uri
                comment = property_object.value
                assert isinstance(comment, str)
            elif property_predicate == RDFS.domain:
                assert domain is None, property_uri
                domain = property_object
                assert isinstance(domain, URIRef)
            elif property_predicate == RDFS.label:
                assert label is None, property_uri
                label = property_object.value
                assert isinstance(label, str)
            elif property_predicate == RDFS.range:
                assert range is None, property_uri
                range = property_object
                assert isinstance(range, URIRef)
            elif property_predicate == RDFS.subPropertyOf:
                sub_property_of.append(property_object)
                assert isinstance(sub_property_of[-1], URIRef)
            elif property_predicate == SKOS.notation:
                assert notation is None, property_uri
                notation = property_object.value
            else:
                self.__logger.warning(
                    "unhandled property (%s) predicate: %s, %s (%s)",
                    property_uri,
                    property_predicate,
                    property_object,
                    type(property_object),
                )

        assert property_types
        if len(property_types) == 1:
            property_type = property_types[0]
        else:
            assert len(property_types) == 2, property_uri
            property_types.remove(PropertyType.OBJECT)
            property_type = property_types[0]
            assert property_type in (
                PropertyType.FUNCTIONAL,
                PropertyType.INVERSE_FUNCTIONAL,
                PropertyType.SYMMETRIC,
                PropertyType.TRANSITIVE,
            ), property_uri

        return Property(
            comment=comment,
            domain=domain,
            inverse_of=inverse_of,
            label=label,
            notation=notation,
            range=range,
            sub_property_of=tuple(sub_property_of),
            type=property_type,
            uri=property_uri,
        )

    def __parse_property_restriction(
        self, *, graph: Graph, property_restriction_uri: URIRef
    ) -> PropertyRestriction:
        cardinality = None
        on_property = None
        max_cardinality = None
        min_cardinality = None
        some_values_from = None
        for (restriction_predicate, restriction_object,) in graph.predicate_objects(
            property_restriction_uri
        ):
            if restriction_predicate == RDF.type:
                assert restriction_object == OWL.Restriction
            elif restriction_predicate == OWL.cardinality:
                cardinality = restriction_object.toPython()
                assert isinstance(cardinality, int)
            elif restriction_predicate == OWL.onProperty:
                on_property = restriction_object
                assert isinstance(on_property, URIRef)
            elif restriction_predicate == OWL.maxCardinality:
                max_cardinality = restriction_object.toPython()
                assert isinstance(max_cardinality, int)
            elif restriction_predicate == OWL.minCardinality:
                min_cardinality = restriction_object.toPython()
                assert isinstance(min_cardinality, int)
            elif restriction_predicate == OWL.someValuesFrom:
                some_values_from = restriction_object
                assert isinstance(some_values_from, URIRef)
            else:
                raise NotImplementedError(restriction_predicate)
        assert on_property is not None
        return PropertyRestriction(
            cardinality=cardinality,
            max_cardinality=max_cardinality,
            min_cardinality=min_cardinality,
            on_property=on_property,
            some_values_from=some_values_from,
        )
