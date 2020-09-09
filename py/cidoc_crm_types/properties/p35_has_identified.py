from .p141_assigned import P141Assigned
from dataclasses import dataclass


@dataclass
class P35HasIdentified(P141Assigned):
    """
Scope note:
This property identifies the E3 Condition State that was observed in an E14 Condition Assessment activity.


Examples:
- 1997 condition assessment of silver cup 232 (E14) has identified oxidation traces were present in 1997 (E3) has type oxidation traces (E55)


In First Order Logic:
P35(x,y) &#8835;E14(x)
P35(x,y) &#8835; E3(y)
P35(x,y) &#8835; P141(x,y)
    """

    URI = "http://erlangen-crm.org/current/P35_has_identified"
