from typing import NamedTuple, Optional, Tuple

from rdflib import URIRef

from cidoc_crm_types_generator.property_type import PropertyType


class Property(NamedTuple):
    comment: Optional[str]
    domain: Optional[URIRef]
    inverse_of: Optional[URIRef]
    label: Optional[str]
    notation: Optional[str]
    range: Optional[URIRef]
    sub_property_of: Tuple[URIRef, ...]
    type: PropertyType
    uri: URIRef
