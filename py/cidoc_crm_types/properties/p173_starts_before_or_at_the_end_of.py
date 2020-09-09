from dataclasses import dataclass


@dataclass
class P173StartsBeforeOrAtTheEndOf:
    """
Scope note:
This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity starts before or simultaneously with the end of the temporal extent of the range instance B of E2 Temporal Entity.
In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Astart &#8804; Bend is true.

This property is part of the set of temporal primitives P173 &#8211; P176, P182 &#8211; P185.

This property corresponds to the disjunction (logical OR) of the following Allen temporal relations [Allen, 1983]: {before, meets, met-by, overlaps, starts, started-by, contains, finishes, finished-by, equals, during,  overlapped by}


In First Order Logic:
P173(x,y) &#8835; E2(x)
P173(x,y) &#8835; E2(y)
    """

    URI = "http://erlangen-crm.org/current/P173_starts_before_or_at_the_end_of"
