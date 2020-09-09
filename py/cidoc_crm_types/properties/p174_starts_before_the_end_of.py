from .p173_starts_before_or_at_the_end_of import P173StartsBeforeOrAtTheEndOf
from dataclasses import dataclass


@dataclass
class P174StartsBeforeTheEndOf(P173StartsBeforeOrAtTheEndOf):
    """
Scope note:
This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity starts definitely before the end of the temporal extent of the range instance B of E2 Temporal Entity.  
In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Astart < Bend is true. 

This property is part of the set of temporal primitives P173 &#8211; P176, P182 &#8211; P185.

This property corresponds to a disjunction (logical OR) of the following Allen temporal relations [Allen, 1983] :{before, meets, overlaps, starts, started-by, contains, finishes, finished-by, equals, during,  overlapped by}

Typically, this property is a consequence of a known influence of some event on another event or activity, such as a novel written by someone being continued by someone else, or the knowledge of a defeat on a distant battlefield causing people to end their ongoing activities.


In First Order Logic:
P174(x,y) &#8835; E2(x)
P174(x,y) &#8835; E2(y)
P174(x,y) &#8835; P173(x,y)
    """

    URI = "http://erlangen-crm.org/current/P174_starts_before_the_end_of"
