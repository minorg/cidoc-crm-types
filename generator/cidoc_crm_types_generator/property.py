from typing import NamedTuple, Optional, Tuple

from rdflib import URIRef


class Property(NamedTuple):
    comment: Optional[str]
    domain: Optional[URIRef]
    inverse_of: Optional[URIRef]
    label: Optional[str]
    notation: Optional[str]
    range: Optional[URIRef]
    sub_property_of: Tuple[URIRef, ...]
    uri: URIRef
