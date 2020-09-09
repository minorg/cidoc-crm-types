from .p1_is_identified_by import P1IsIdentifiedBy
from dataclasses import dataclass


@dataclass
class P48HasPreferredIdentifier(P1IsIdentifiedBy):
    """
Scope note:
This property records the preferred instance of E42 Identifier that was used to identify an instance of E1 CRM Entity at the time this property was recorded.

More than one preferred identifier may have been assigned to an item over time. Use of this property requires an external mechanism for assigning temporal validity to the respective
CIDOC CRM instance.

The fact that an identifier is a preferred one for an organisation can be better expressed in a context independent form by assigning a suitable instance of E55 Type to the respective instance of E15 Identifier Assignment using the P2 has type property.


Examples:
- the pair of Lederhosen donated by Dr Martin Doerr (E22) has preferred identifier "OXCMS:2001.1.32" (E42)


In First Order Logic:
P48(x,y) &#8835; E1(x)
P48(x,y) &#8835; E42(y)
P48(x,y) &#8835; P1(x,y)
    """

    URI = "http://erlangen-crm.org/current/P48_has_preferred_identifier"
