from dataclasses import dataclass


@dataclass
class P26MovedTo:
    """
Scope note:
This property identifies a destination, an instance of E53 place, of an instance of E9 Move.

A move will be linked to a destination, such as the move of an artifact from storage to display. A move may be linked to many terminal instances of E53 Place by multiple instances of this property. In this case the move describes a distribution of a set of objects. The area of the move includes the origin(s), route and destination(s).

Therefore the described destination is an instance of E53 Place which P89 falls within (contains) the instance of E53 Place the move P7 took place at.


Examples:
- the movement of Tut-Ankh-Amun Exhibition (E9) moved to The British Museum (E53)


In First Order Logic:
P26(x,y) &#8835; E9(x)
P26(x,y) &#8835; E53(y)
P26(x,y) &#8835; (&#8707;z)[ E53(z) &#8743; P7(x,z) &#8743; P89(y,z)]
    """

    URI = "http://erlangen-crm.org/current/P26_moved_to"
