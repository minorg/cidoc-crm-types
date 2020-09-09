from .p175_starts_before_or_with_the_start_of import P175StartsBeforeOrWithTheStartOf
from dataclasses import dataclass


@dataclass
class P176StartsBeforeTheStartOf(P175StartsBeforeOrWithTheStartOf):
    """
Scope note:
This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity starts definitely before the start of the temporal extent of the range instance B of E2 Temporal Entity. 
 In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Astart < Bstart is true. 

This property is part of the set of temporal primitives P173 &#8211; P176, P182 &#8211; P185.


This property corresponds to a disjunction (logical OR) of the following Allen temporal relations [Allen, 1983]: {before, meets, overlaps, contains, finished-by}


In First Order Logic:
P176(x,y) &#8835; E2(x)
P176(x,y) &#8835; E2(y)
P176(x,y) &#8835; P175(x,y)
    """

    URI = "http://erlangen-crm.org/current/P176_starts_before_the_start_of"
