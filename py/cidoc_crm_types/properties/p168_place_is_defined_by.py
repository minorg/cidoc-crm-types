from dataclasses import dataclass


@dataclass
class P168PlaceIsDefinedBy:
    """
Scope note:
This property associates an instance of E53 Place with an instance of E94 Space Primitive that defines it. Syntactic variants or use of different scripts may result in multiple instances of E94 Space Primitive defining exactly the same place. Transformations between different reference systems always result in new definitions of places approximating each other and not in alternative definitions.


In First Order Logic:
P168(x,y) &#8835; E53(x)
P168(x,y) &#8835; E94(y)
    """

    URI = "http://erlangen-crm.org/current/P168_place_is_defined_by"
