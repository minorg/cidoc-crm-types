from .p12_occurred_in_the_presence_of import P12OccurredInThePresenceOf
from dataclasses import dataclass


@dataclass
class P113Removed(P12OccurredInThePresenceOf):
    """
Scope note:
This property identifies the instance of E18 Physical Thing that is removed during an instance of E80 Part Removal activity.


Examples:
- the opening of the coffin of Tut-Ankh-Amun (E80) removed The mummy of Tut-Ankh-Amun (E20,E22)


In First Order Logic:
P113(x,y) &#8835; E80(x)
P113(x,y) &#8835; E18(y)
P113(x,y) &#8835; P12(x,y)
    """

    URI = "http://erlangen-crm.org/current/P113_removed"
