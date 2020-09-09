from .p182_ends_before_or_at_the_start_of import P182EndsBeforeOrAtTheStartOf
from dataclasses import dataclass


@dataclass
class P183EndsBeforeTheStartOf(P182EndsBeforeOrAtTheStartOf):
    """
Scope note:
This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity ends definitely before the start of the temporal extent of the range instance B of E2 Temporal Entity. 
In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Aend < Bstart  is true. 

This property is part of the set of temporal primitives P173 &#8211; P176, P182 &#8211; P185.

This property corresponds to a disjunction (logical OR) of the following Allen temporal relations [Allen, 1983]: {before}


In First Order Logic:
P183(x,y) &#8835; E2(x)
P183(x,y) &#8835; E2(y)
P183(x,y) &#8835; P182(x,y)
    """

    URI = "http://erlangen-crm.org/current/P183_ends_before_the_start_of"
