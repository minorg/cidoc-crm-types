from typing import Dict, NamedTuple, Tuple

from rdflib import URIRef

from cidoc_crm_types_generator.entity_class import EntityClass
from cidoc_crm_types_generator.property import Property


class EcrmOwl(NamedTuple):
    entity_classes_by_uri: Dict[URIRef, EntityClass]
    properties_by_uri: Dict[URIRef, Property]
