from typing import NamedTuple, Optional, Tuple

from rdflib import URIRef

from cidoc_crm_types_generator.property_restriction import PropertyRestriction


class EntityClass(NamedTuple):
    comment: Optional[str]
    disjoint_with: Optional[URIRef]
    label: Optional[str]
    notation: Optional[str]
    property_restrictions: Tuple[PropertyRestriction, ...]
    sub_class_of: Tuple[URIRef, ...]
    uri: URIRef
