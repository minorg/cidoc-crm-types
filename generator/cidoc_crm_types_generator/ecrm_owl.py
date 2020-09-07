from typing import NamedTuple, Tuple

from cidoc_crm_types_generator.entity_class import EntityClass
from cidoc_crm_types_generator.property import Property


class EcrmOwl(NamedTuple):
    entity_classes: Tuple[EntityClass, ...]
    properties: Tuple[Property, ...]
