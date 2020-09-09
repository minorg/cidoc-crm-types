from .p105_right_held_by import P105RightHeldBy
from .p51_has_former_or_current_owner import P51HasFormerOrCurrentOwner
from dataclasses import dataclass


@dataclass
class P52HasCurrentOwner(P51HasFormerOrCurrentOwner, P105RightHeldBy):
    """
Scope note:
This property identifies the instance of E21 Person or E74 Group that was the owner of an instance of E18 Physical Thing at the time of validity of the record or database containing the statement that uses this property.

P52 has current owner (is current owner of) is a shortcut for the more detailed path from &#8216;E18 Physical Thing through&#8217;, &#8216;P24i changed ownership through, &#8216;E8 Acquisition&#8217;, &#8216;P22 transferred title to&#8217;, to &#8216;E39 Actor&#8217;, if and only if this acquisition event is the most recent.


Examples:
- paintings from the Iveagh Bequest (E18) has current owner &#171;English Heritage&#187; (E74)


In First Order Logic:
P52 (x,y) &#8835; E18(x)
P52 (x,y) &#8835; E39(y)
P52(x,y) &#8835; P51(x,y)
P52(x,y) &#8835; P105(x,y)
    """

    URI = "http://erlangen-crm.org/current/P52_has_current_owner"
