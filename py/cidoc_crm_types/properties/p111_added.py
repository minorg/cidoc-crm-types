from .p16_used_specific_object import P16UsedSpecificObject
from dataclasses import dataclass


@dataclass
class P111Added(P16UsedSpecificObject):
    """
Scope note:
This property identifies the instance of E18 Physical Thing that is added during an instance of E79 Part Addition activity


Examples:
- the insertion of the final nail (E79) added the last nail in George VI's coffin (E18)


In First Order Logic:
P111(x,y) &#8835; E79(x)
P111(x,y) &#8835; E18(y)
P111(x,y) &#8835; P12(x,y)
P111(x,y) &#8835; P16(x,y)
    """

    URI = "http://erlangen-crm.org/current/P111_added"
