from .p93_took_out_of_existence import P93TookOutOfExistence
from dataclasses import dataclass


@dataclass
class P124Transformed(P93TookOutOfExistence):
    """
Scope note:
This property identifies the instance or instances E18 Physical Thing that have ceased to exist due to an instance of E81 Transformation.
The item that has ceased to exist and was replaced by the result of the Transformation. The continuity between both items, the new and the old, is expressed by the links to the common instance of E81 Transformation.


Examples:
- the transformation of the Venetian Loggia in Heraklion into a city hall (E81) transformed the Venetian Loggia in Heraklion (E22)
- the death and mummification of Tut-Ankh-Amun (E81) transformed the ruling Pharao Tut-Ankh-Amun (E21)


In First Order Logic:
P124(x,y) &#8835; E81(x)
P124(x,y) &#8835; E77(y)
P124(x,y) &#8835; P93(x,y)
    """

    URI = "http://erlangen-crm.org/current/P124_transformed"
