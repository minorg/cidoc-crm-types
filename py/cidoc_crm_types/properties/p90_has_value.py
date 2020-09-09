from dataclasses import dataclass


@dataclass
class P90HasValue:
    """
Scope note:
This property allows an instance of E54 Dimension to be approximated by an instance of E60 Number
primitive.


Examples:
- height of silver cup 232 (E54) has value 226 (E60)


In First Order Logic:
P90(x,y) &#8835; E54(x)
P90(x,y) &#8835; E60(y)
    """

    URI = "http://erlangen-crm.org/current/P90_has_value"
