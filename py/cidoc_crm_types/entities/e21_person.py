from .e20_biological_object import E20BiologicalObject
from .e39_actor import E39Actor
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E21Person(E39Actor, E20BiologicalObject):
    P152_has_parent: Tuple[object, ...] = ()  # Range: E21Person
    P152_is_parent_of: Tuple[object, ...] = ()  # Range: E21Person
    P97_was_father_for: Tuple[object, ...] = ()  # Range: E67Birth
