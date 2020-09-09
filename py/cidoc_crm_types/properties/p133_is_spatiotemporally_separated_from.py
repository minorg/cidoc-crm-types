from dataclasses import dataclass


@dataclass
class P133IsSpatiotemporallySeparatedFrom:
    """
Scope note:
This symmetric property associates two instances of E92 Spacetime Volume that have no extents in common. If only the fuzzy boundaries of the instances of E92 Spacetime Volume overlap, this property cannot be determined from observation alone and therefore should not be applied. However, there may be other forms of justification that the two instances of E92 Spacetime Volume must not have any of their extents in common regardless of where and when precisely.

If this property holds for two instances of E92 Spacetime Volume then it cannot be the case that P132 spatiotemporally overlaps with also holds for the same two instances. Furthermore, there are cases where neither P132 nor P133 holds between two instances of E92 Spacetime Volume. This would occur where only an overlap of the fuzzy boundaries of the two instances of E92 Spacetime Volume occurs and no other evidence is available.


Examples:
- the &#8220;Hallstatt&#8221; period (E4) is spatiotemporally separated from the &#8220;La T&#232;ne&#8221; era (E4)
- Kingdom of Greece (1831-1924) (E92) is spatiotemporally separated from Ottoman Empire (1299-1922) (E92)
- The path of the army of Alexander (335-323 B.C.) (E92) is spatiotemporally separated from the Mauryan Empire (E92)


In First Order Logic:
P133(x,y) &#8835; E92(x) 
P133(x,y) &#8835; E92(y) 
P133(x,y) &#8835; P133(y,x)
P133(x,y) &#8835; &#172;P132(x,y)
    """

    URI = "http://erlangen-crm.org/current/P133_is_spatiotemporally_separated_from"
