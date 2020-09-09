from dataclasses import dataclass


@dataclass
class P101HadAsGeneralUse:
    """
Scope note:
This property associates an instance of E70 Thing with an instance of E55 Type describing its general usage.

It allows the relationship between particular things, both physical and immaterial, and general methods and techniques of use to be documented. Thus it can be asserted that a baseball bat had a general use for sport and a specific use for threatening people during the Great Train Robbery.


Examples:
- Tony Gill's Ford Mustang (E22) had as general use transportation (E55)


In First Order Logic:
P101(x,y) &#8835; E70(x)
P101(x,y) &#8835; E55(y)
P101(x,y) &#8835; (&#8707;z)[E7(z) &#8743; P16(z,x) &#8743; P2(z,y)]
    """

    URI = "http://erlangen-crm.org/current/P101_had_as_general_use"
