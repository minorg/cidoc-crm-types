from .p10_falls_within import P10FallsWithin
from dataclasses import dataclass


@dataclass
class P166WasAPresenceOf(P10FallsWithin):
    """
Scope Note:
This property associates an instance of E93 Presence with the instance of E92 Spacetime Volume of which it represents a temporal restriction (i.e.: a time-slice). Instantiating this property constitutes a necessary part of the identity of the respective instance of E93 Presence. 


In First Order Logic:
P166(x,y) &#8835; E93(x)
P166(x,y) &#8835; E92(y)
P166(x,y) &#8835; P10(x,y)
    """

    URI = "http://erlangen-crm.org/current/P166_was_a_presence_of"
