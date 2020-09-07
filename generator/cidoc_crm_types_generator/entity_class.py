from dataclasses import dataclass
from typing import NamedTuple, Optional, Tuple

from rdflib import URIRef

from cidoc_crm_types_generator._model import _Model
from cidoc_crm_types_generator.property_restriction import PropertyRestriction


@dataclass(frozen=True)
class EntityClass(_Model):
    disjoint_with: Optional[URIRef]
    notation: Optional[str]
    property_restrictions: Tuple[PropertyRestriction, ...]
    sub_class_of: Tuple[URIRef, ...]
