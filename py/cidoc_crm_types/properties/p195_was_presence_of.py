from dataclasses import dataclass


@dataclass
class P195WasPresenceOf:
    """
Scope note: 
This property associates an instance of E93 Presence with the instance of E18 Physical Thing of which it represents a temporal restriction (i.e.: a time-slice) of the thing&#8217;s trajectory through spacetime. In other words, it describes where the instance of E18 Physical Thing were or moved around within a given time-span. Instantiating this property constitutes a necessary part of the identity of the respective instance of E93 Presence.

This property is a shortcut of the fully developed path from E18 Physical Thing through P196 defines, E92 Spacetime Volume, P166 was a presence of (had presence), E93 Presence.


In First Order Logic:
P195(x,y) &#8835; E93(x)
P195(x,y) &#8835; E18(y)
P195(x,y) = (&#8707;z)[E9(z) &#8743; P196 (y,z) &#8743; P166(z,x)]
    """

    URI = "http://erlangen-crm.org/current/P195_was_presence_of"
