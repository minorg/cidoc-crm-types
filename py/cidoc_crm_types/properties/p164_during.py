from .p160_has_temporal_projection import P160HasTemporalProjection
from dataclasses import dataclass


@dataclass
class P164During(P160HasTemporalProjection):
    """
Scope note:
This property relates an instance of E93 Presence with the chosen instance of E52 Time-Span that defines the time-slice of the spacetime volume that this instance of E93 Presence is related to by the property P166 was a presence of (had presence).


Examples:
- 2016-02-09 (E52) was time-span of the last day of the 2016 Carnival in Cologne (E93).


In First Order Logic:
P164 (x,y) &#8835; E93(x)
P164 (x,y) &#8835; E52(y)
P164 (x,y) &#8835; P160(x,y)
    """

    URI = "http://erlangen-crm.org/current/P164_during"
