from .p15_was_influenced_by import P15WasInfluencedBy
from dataclasses import dataclass


@dataclass
class P17WasMotivatedBy(P15WasInfluencedBy):
    """
Scope note:
This property describes an item or items that are regarded as a reason for carrying out the E7 Activity.

For example, the discovery of a large hoard of treasure may call for a celebration, an order from head quarters can start a military manoeuvre.


Examples:
- the resignation of the chief executive (E7) was motivated by the collapse of Swiss Air (E68).
- the coronation of Elizabeth II (E7) was motivated by the death of George VI (E69)


In First Order Logic:
P17(x,y) &#8835; E7(x)
P17(x,y) &#8835; E1(y)
P17 (x,y) &#8835; P15(x,y)
    """

    URI = "http://erlangen-crm.org/current/P17_was_motivated_by"
