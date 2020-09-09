from dataclasses import dataclass


@dataclass
class P121OverlapsWith:
    """
Scope note:
This symmetric property associates an instance of E53 Place with another instance of E53 Place geometrically overlapping it.

It does not specify anything about the shared area. This property is purely spatial, in contrast to the temporal overlaps described by pxxx, pxxy or pxxz, and and, spatio temporal overlaps described by p132 spatiotemporally overlaps with.


Examples:
- the territory of the United States (E53) overlaps with the Arctic (E53)
- The maximal extent of the Greek Kingdom (E53) overlaps with the maximal extent of the Ottoman Empire(E53)


In First Order Logic:
P121(x,y) &#8835; E53(x)
P121(x,y) &#8835; E53(y)
P121(x,y) &#8835; P121(y,x)
    """

    URI = "http://erlangen-crm.org/current/P121_overlaps_with"
