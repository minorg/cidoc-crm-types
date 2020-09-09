from .p132_spatiotemporally_overlaps_with import P132SpatiotemporallyOverlapsWith
from dataclasses import dataclass


@dataclass
class P9ConsistsOf(P132SpatiotemporallyOverlapsWith):
    """
Scope note:
This property associates an instance of E4 Period with another instance of E4 Period that is defined by a subset of the phenomena that define the former. Therefore the spacetime volume of the latter must fall within the spacetime volume of the former.
This property is transitive.


Examples:
- Cretan Bronze Age (E4) consists of Middle Minoan (E4)


In First Order Logic:
P9(x,y) &#8835; E4(x)
P9(x,y) &#8835; E4(y)
P9(x,y) &#8835; P10(y,x)
    """

    URI = "http://erlangen-crm.org/current/P9_consists_of"
