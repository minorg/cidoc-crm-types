from dataclasses import dataclass


@dataclass
class P160HasTemporalProjection:
    """
Scope note:
This property describes the temporal projection of an instance of E92 Spacetime Volume. The property P4 has time-span is the same as P160 has temporal projection if it is used to document an instance of E4 Period or any subclass of it.


Example:


In First Order Logic:
P160(x,y) &#8835; E92(x)
P160(x,y)&#8835; E52(y)
    """

    URI = "http://erlangen-crm.org/current/P160_has_temporal_projection"
