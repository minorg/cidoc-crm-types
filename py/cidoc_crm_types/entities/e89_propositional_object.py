from .e28_conceptual_object import E28ConceptualObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E89PropositionalObject(E28ConceptualObject):
    P129_is_about: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P148_has_component: Tuple[object, ...] = ()  # Range: E89PropositionalObject
    P148_is_component_of: Tuple[object, ...] = ()  # Range: E89PropositionalObject
    P67_refers_to: Tuple[object, ...] = ()  # Range: E1CRMEntity
