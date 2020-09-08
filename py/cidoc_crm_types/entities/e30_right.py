from .e89_propositional_object import E89PropositionalObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E30Right(E89PropositionalObject):
    P104_applies_to: Tuple[object, ...] = ()  # Range: E72LegalObject
    P75_is_possessed_by: Tuple[object, ...] = ()  # Range: E39Actor
