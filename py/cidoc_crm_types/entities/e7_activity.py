from .e5_event import E5Event
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E7Activity(E5Event):
    P125_used_object_of_type: Tuple[object, ...] = ()  # Range: E55Type
    P15_was_influenced_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P17_was_motivated_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P19_was_intended_use_of: Tuple[object, ...] = ()  # Range: E71ManMadeThing
    P20_had_specific_purpose: Tuple[object, ...] = ()  # Range: E5Event
    P21_had_general_purpose: Tuple[object, ...] = ()  # Range: E55Type
    P32_used_general_technique: Tuple[object, ...] = ()  # Range: E55Type
