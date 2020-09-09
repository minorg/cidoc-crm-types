from dataclasses import dataclass


@dataclass
class P132SpatiotemporallyOverlapsWith:
    """
Scope note:
This symmetric property associates two instances of E92 Spacetime Volume that have some of their extents in common. If only the fuzzy boundaries of the instances of E92 Spacetime Volume overlap, this property cannot be determined from observation alone and therefore should not be applied. However, there may be other forms of justification that the two instances of E92 Spacetime Volume must have some of their extents in common regardless of where and when precisely.

If this property holds for two instances of E92 Spacetime Volume then it cannot be the case that P133 also holds for the same two instances. Furthermore, there are cases where neither P132 nor P133 holds between two instances of E92 Spacetime Volume. This would occur where only an overlap of the fuzzy boundaries of the two instances of E92 Spacetime Volume occurs and no other evidence is available.


Examples:
- the &#8220;Urnfield&#8221; period (E4) spatiotemporally overlaps with the &#8220;Hallstatt&#8221; period (E4)


In First Order Logic: 
P132(x,y) &#8835; E92(x) 
P132(x,y) &#8835; E92(y) 
P132(x,y) &#8835; P132(y,x)
P132(x,y) &#8835; &#172;P133(x,y)
    """

    URI = "http://erlangen-crm.org/current/P132_spatiotemporally_overlaps_with"
