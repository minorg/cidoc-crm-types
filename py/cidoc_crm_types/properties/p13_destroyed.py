from .p93_took_out_of_existence import P93TookOutOfExistence
from dataclasses import dataclass


@dataclass
class P13Destroyed(P93TookOutOfExistence):
    """
Scope note:
This property links an instance of E6 Destruction to an instance of E18 Physical Thing that has been destroyed by it.

Destruction implies the end of an item&#8217;s life as a subject of cultural documentation &#8211; the physical matter of which the item was composed may in fact continue to exist. An instance of E6 Destruction may be contiguous with an instance of E12 Production that brings into existence a derived object composed partly of matter from the destroyed object.


Examples:
- the Tay Bridge Desaster (E6) destroyed The Tay Bridge (E22)


In First Order Logic:
P13 (x,y) &#8835; E6 (x)
P13 (x,y) &#8835; E18(y)
P13 (x,y) &#8835; P93(x,y)
    """

    URI = "http://erlangen-crm.org/current/P13_destroyed"
