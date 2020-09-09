from .p92_brought_into_existence import P92BroughtIntoExistence
from dataclasses import dataclass


@dataclass
class P98BroughtIntoLife(P92BroughtIntoExistence):
    """
Scope note:
This property links an instance of E67 Birth event to an instance of E21 Person in the role of offspring.

Twins, triplets etc. are brought into life by the same instance of E67 Birth. This is not intended for use with general Natural History material, only people. There is no explicit method for modelling conception and gestation except by using extensions.


Examples:
- the Birth of Queen Elizabeth II (E67) brought into life Queen Elizabeth II (E21)


In First Order Logic:
P98(x,y) &#8835; E67(x)
P98(x,y) &#8835; E21(y)
P98(x,y) &#8835; P92(x,y)
    """

    URI = "http://erlangen-crm.org/current/P98_brought_into_life"
