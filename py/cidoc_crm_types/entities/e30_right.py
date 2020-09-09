from .e89_propositional_object import E89PropositionalObject
from dataclasses import dataclass


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
E30(x) &#8835; E89(x
    """

    TYPE_URI = "http://erlangen-crm.org/current/E30_Right"
