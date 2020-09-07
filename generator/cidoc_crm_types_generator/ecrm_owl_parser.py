import logging
from typing import Tuple

from rdflib import BNode, Graph, OWL, RDF, RDFS, SKOS, URIRef

from cidoc_crm_types_generator.ecrm_owl import EcrmOwl
from cidoc_crm_types_generator.entity_class import EntityClass
from cidoc_crm_types_generator.property_restriction import PropertyRestriction


class EcrmOwlParser:
    """
    Parser for the Erlangen CRM OWL (http://erlangen-crm.org/)
    """

    def __init__(self):
        self.__logger = logging.getLogger(self.__class__.__name__)

    def parse(self, graph: Graph) -> EcrmOwl:
        entity_classes = self.__parse_entity_classes(graph)
        return EcrmOwl(entity_classes=entity_classes, properties=())

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
        entity_classes = []
        for entity_class_uri in graph.subjects(RDF.type, OWL.Class):
            entity_classes.append(
                self.__parse_entity_class(
                    graph=graph, entity_class_uri=entity_class_uri
                )
            )
        return tuple(entity_classes)

    def __parse_property_restriction(
        self, *, graph: Graph, property_restriction_uri: URIRef
    ):
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
