from dataclasses import dataclass


@dataclass
class P89FallsWithin:
    """
Scope note:
This property identifies an instance of E53 Place that falls wholly within the extent of another instance of E53 Place.

It addresses spatial containment only, and does not imply any relationship between things or phenomena occupying these places.
This property is transitive.


Examples:
- the area covered by the World Heritage Site of Stonehenge (E53) falls within the area of Salisbury Plain (E53)


In First Order Logic:
P89(x,y) &#8835; E53(x)
P89(x,y) &#8835; E53(y)
    """

    URI = "http://erlangen-crm.org/current/P89_falls_within"
