import logging
from typing import Tuple

from rdflib import BNode, Graph, OWL, RDF, RDFS, SKOS, URIRef

from cidoc_crm_types_generator.ecrm_owl import EcrmOwl
from cidoc_crm_types_generator.entity_class import EntityClass
from cidoc_crm_types_generator.property import Property
from cidoc_crm_types_generator.property_restriction import PropertyRestriction


class EcrmOwlParser:
    """
    Parser for the Erlangen CRM OWL (http://erlangen-crm.org/)
    """

    def __init__(self):
        self.__logger = logging.getLogger(self.__class__.__name__)

    def parse(self, graph: Graph) -> EcrmOwl:
        entity_classes = self.__parse_entity_classes(graph)
        properties = self.__parse_properties(graph)
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
                    sub_class_of.append(URIRef)
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
        return tuple(
            self.__parse_property(graph=graph, property_uri=property_uri)
            for property_uri in graph.subjects(RDF.type, OWL.ObjectProperty)
        )

    def __parse_property(self, *, graph: Graph, property_uri: URIRef) -> Property:
        comment = None
        domain = None
        inverse_of = None
        label = None
        notation = None
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
                continue
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
        return Property(
            comment=comment,
            domain=domain,
            inverse_of=inverse_of,
            label=label,
            notation=notation,
            range=range,
            sub_property_of=tuple(sub_property_of),
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
