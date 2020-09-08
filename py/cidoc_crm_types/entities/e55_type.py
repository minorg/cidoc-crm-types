from .e28_conceptual_object import E28ConceptualObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E55Type(E28ConceptualObject):
    P101_was_use_of: Tuple[object, ...] = ()  # Range: E70Thing
    P103_was_intention_of: Tuple[object, ...] = ()  # Range: E71ManMadeThing
    P125_was_type_of_object_used_in: Tuple[object, ...] = ()  # Range: E7Activity
    P127_has_broader_term: Tuple[object, ...] = ()  # Range: E55Type
    P127_has_narrower_term: Tuple[object, ...] = ()  # Range: E55Type
    P137_is_exemplified_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P150_defines_typical_parts_of: Tuple[object, ...] = ()  # Range: E55Type
    P150_defines_typical_wholes_for: Tuple[object, ...] = ()  # Range: E55Type
    P21_was_purpose_of: Tuple[object, ...] = ()  # Range: E7Activity
    P2_is_type_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P32_was_technique_of: Tuple[object, ...] = ()  # Range: E7Activity
    P42_was_assigned_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
