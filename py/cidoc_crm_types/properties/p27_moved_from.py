from dataclasses import dataclass


@dataclass
class P27MovedFrom:
    """
Scope note:
This property identifies an origin, an instance of E53 Place, of an instance of E9 Move.

A move will be linked to an origin, such as the move of an artifact from storage to display. A move may be linked to many starting instances of E53 Place by multiple instances of this property. In this case the move describes the picking up of a set of objects. The area of the move includes the origin(s), route and destination(s).

Therefore the described origin is an instance of E53 Place which P89 falls within (contains) the instance of E53 Place the move P7 took place at.


Examples:
- the movement of Tut-Ankh-Amun Exhibition (E9) moved from The Egyptian Museum in Cairo (E53)


In First Order Logic:
P27(x,y) &#8835; E9(x)
P27(x,y) &#8835; E53(y)
P27(x,y) &#8835; (&#8707;z)[ E53(z) &#8743; P7(x,z) &#8743; P89(y,z)]
    """

    URI = "http://erlangen-crm.org/current/P27_moved_from"
