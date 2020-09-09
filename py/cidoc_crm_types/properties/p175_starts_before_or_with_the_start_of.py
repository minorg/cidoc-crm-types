from .p174_starts_before_the_end_of import P174StartsBeforeTheEndOf
from dataclasses import dataclass


@dataclass
class P175StartsBeforeOrWithTheStartOf(P174StartsBeforeTheEndOf):
    """
Scope note:
This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity starts before or simultaneously with the start of the temporal extent of the range instance B of E2 Temporal Entity. 
 In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Astart &#8804; Bstart is true.

This property is part of the set of temporal primitives P173 &#8211; P176, P182 &#8211; P185.

This property corresponds to a disjunction (logical OR) of the following Allen temporal relations [Allen, 1983]: {before, meets, overlaps, starts, started-by, contains, finished-by, equals}


In First Order Logic:
P175(x,y) &#8835; E2(x)
P175(x,y) &#8835; E2(y)
P175(x,y) &#8835; P174(x,y)
    """

    URI = "http://erlangen-crm.org/current/P175_starts_before_or_with_the_start_of"
