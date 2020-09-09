from .p176_starts_before_the_start_of import P176StartsBeforeTheStartOf
from .p185_ends_before_the_end_of import P185EndsBeforeTheEndOf
from dataclasses import dataclass


@dataclass
class P182EndsBeforeOrAtTheStartOf(P185EndsBeforeTheEndOf, P176StartsBeforeTheStartOf):
    """
Scope note:
This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity ends before or simultaneously with the start of the temporal extent of the range instance B of E2 Temporal Entity. 
 In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Aend &#8804; Bstart is true.

This property is part of the set of temporal primitives P173 &#8211; P176, P182 &#8211; P185.

This property corresponds to a disjunction (logical OR) of the following Allen temporal relations [Allen, 1983]: {before, meets}


In First Order Logic:
P182(x,y) &#8835; E2(x)
P182(x,y) &#8835; E2(y)
P182(x,y) &#8835; P176(x,y)
P182(x,y) &#8835; P185(x,y)
    """

    URI = "http://erlangen-crm.org/current/P182_ends_before_or_at_the_start_of"
