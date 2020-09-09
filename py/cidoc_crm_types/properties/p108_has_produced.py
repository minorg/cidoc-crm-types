from .p31_has_modified import P31HasModified
from .p92_brought_into_existence import P92BroughtIntoExistence
from dataclasses import dataclass


@dataclass
class P108HasProduced(P92BroughtIntoExistence, P31HasModified):
    """
Scope note:
This property identifies the instance of E24 Physical Human-Made Thing that came into existence as a result of the instance of E12 Production.

The identity of an instance of E24 Physical Human-Made Thing is not defined by its matter, but by its existence as a subject of documentation. An E12 Production can result in the creation of multiple instances of E24 Physical Human-Made Thing.


Examples:
- The building of Rome (E12) has produced &#932;he Colosseum (E22)


In First Order Logic:
P108(x,y) &#8835; E12(x)
P108(x,y) &#8835; E24(y)
P108(x,y) &#8835; P31(x,y)
P108(x,y) &#8835; P92(x,y)
    """

    URI = "http://erlangen-crm.org/current/P108_has_produced"
