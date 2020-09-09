from .p141_assigned import P141Assigned
from dataclasses import dataclass


@dataclass
class P37Assigned(P141Assigned):
    """
Scope note:
This property records the identifier that was assigned to an item in an instance of P37 Identifier Assignment.
The same identifier may be assigned on more than one occasion.
An Identifier might be created prior to an assignment.


Examples:
- 01 June 1997 Identifier Assignment of the silver cup donated by Martin Doerr (E15) assigned "232" (E42)


In First Order Logic:
P37(x,y) &#8835; E15(x)
P37(x,y) &#8835; E42(y)
P37(x,y) &#8835; P141(x,y)
    """

    URI = "http://erlangen-crm.org/current/P37_assigned"
