from dataclasses import dataclass
from typing import NamedTuple, Optional, Tuple

from rdflib import URIRef

from cidoc_crm_types_generator._model import _Model
from cidoc_crm_types_generator.property_type import PropertyType


@dataclass(frozen=True)
class Property(_Model):
    domain: Optional[URIRef]
    inverse_of: Optional[URIRef]
    notation: Optional[str]
    range: Optional[URIRef]
    sub_property_of: Tuple[URIRef, ...]
    type: PropertyType
