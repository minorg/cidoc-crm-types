from dataclasses import dataclass


@dataclass
class P91HasUnit:
    """
Scope note:
This property shows the type of unit an instance of E54 Dimension was expressed in.


Examples:
- height of silver cup 232 (E54) has unit mm (E58)


In First Order Logic:
P91(x,y) &#8835; E54(x)
P91(x,y) &#8835; E58(y)
    """

    URI = "http://erlangen-crm.org/current/P91_has_unit"
