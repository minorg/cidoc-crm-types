from dataclasses import dataclass


@dataclass
class P122BordersWith:
    """
Scope note:
This symmetric property associates an instance of E53 Place with another instance of E53 Place which shares a part of its borders.

This property is purely spatial, in contrast to time properties, which are purely temporal.


Examples:
- Scotland (E53) borders with England (E53)


In First Order Logic:
P122(x,y) &#8835; E53(x)
P122(x,y) &#8835; E53(y)
P122(x,y) &#8835; P122(y,x)
    """

    URI = "http://erlangen-crm.org/current/P122_borders_with"
