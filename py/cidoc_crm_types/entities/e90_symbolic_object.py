from .e28_conceptual_object import E28ConceptualObject
from .e72_legal_object import E72LegalObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E90SymbolicObject(E28ConceptualObject, E72LegalObject):
    P106_forms_part_of: Tuple[object, ...] = ()  # Range: E90SymbolicObject
    P106_is_composed_of: Tuple[object, ...] = ()  # Range: E90SymbolicObject
    P165i_is_incorporated_in: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P190_has_symbolic_content: Tuple[object, ...] = ()  # Range: object
