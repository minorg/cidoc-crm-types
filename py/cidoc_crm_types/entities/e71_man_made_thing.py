from .e70_thing import E70Thing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E71ManMadeThing(E70Thing):
    P102_has_title: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P103_was_intended_for: Tuple[object, ...] = ()  # Range: E55Type
    P19_was_made_for: Tuple[object, ...] = ()  # Range: E7Activity
