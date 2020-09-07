from typing import NamedTuple, Optional

from rdflib import URIRef


class PropertyRestriction(NamedTuple):
    cardinality: Optional[int]
    max_cardinality: Optional[int]
    min_cardinality: Optional[int]
    on_property: URIRef
    some_values_from: Optional[URIRef]
