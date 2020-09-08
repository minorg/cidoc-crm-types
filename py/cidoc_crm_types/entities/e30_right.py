from .e89_propositional_object import E89PropositionalObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E30Right(E89PropositionalObject):
    """
Scope note:
This class comprises legal privileges concerning material and immaterial things or their derivatives.

These include reproduction and property rights.


Examples:
- Copyright held by ISO on ISO/CD 21127
- ownership of the "Mona Lisa" by the Louvre


In First Order Logic:
E30(x) ? E89(x
    """

    P104_applies_to: Tuple[object, ...] = ()  # Range: E72LegalObject
    P75_is_possessed_by: Tuple[object, ...] = ()  # Range: E39Actor
