from .p92_brought_into_existence import P92BroughtIntoExistence
from dataclasses import dataclass


@dataclass
class P123ResultedIn(P92BroughtIntoExistence):
    """
Scope note:
This property identifies the instance or instances of E18 Physical Thing that are the result of an instance of E81 Transformation. New items replace the transformed item or items, which cease to exist as units of documentation. The physical continuity between the old and the new is expressed by the links to the common instance of E81 Transformation


Examples:
- the transformation of the Venetian Loggia in Heraklion into a city hall (E81)  resulted in the City Hall of Heraklion (E22)
- the death and mummification of Tut-Ankh-Amun (E81) resulted in the Mummy of Tut Tut-Ankh-Amun (E22 and E20)


In First Order Logic:
P123(x,y) &#8835; E81(x)
P123(x,y) &#8835; E77(y)
P123(x,y) &#8835; P92(x,y)
    """

    URI = "http://erlangen-crm.org/current/P123_resulted_in"
