from .p132_spatiotemporally_overlaps_with import P132SpatiotemporallyOverlapsWith
from dataclasses import dataclass


@dataclass
class P10FallsWithin(P132SpatiotemporallyOverlapsWith):
    """
Scope note:
This property associates an instance of E92 Spacetime Volume with another instance of E92 Spacetime Volume that falls within the latter. In other words, all points in the former are also points in the latter. 
This property is transitive.


Examples:
- the Great Plague (E4) falls within The Gothic period (E4)


In First Order Logic:
P10(x,y) &#8835; E92(x)
P10(x,y) &#8835; E92(y)
P10(x,y) &#8835; P132(x,y)
    """

    URI = "http://erlangen-crm.org/current/P10_falls_within"
