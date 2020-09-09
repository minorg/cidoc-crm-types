from .p12_occurred_in_the_presence_of import P12OccurredInThePresenceOf
from dataclasses import dataclass


@dataclass
class P31HasModified(P12OccurredInThePresenceOf):
    """
Scope note:
This property identifies the instance of E24 Physical Human-Made Thing modified in an instance of E11 Modification.


Examples:
- rebuilding of the Reichstag (E11) has modified the Reichstag in Berlin (E24)


In First Order Logic:
P31(x,y) &#8835; E11(x)
P31(x,y) &#8835; E24(y)
P31(x,y) &#8835; P12(x,y)
    """

    URI = "http://erlangen-crm.org/current/P31_has_modified"
