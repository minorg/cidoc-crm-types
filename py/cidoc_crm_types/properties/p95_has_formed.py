from .p92_brought_into_existence import P92BroughtIntoExistence
from dataclasses import dataclass


@dataclass
class P95HasFormed(P92BroughtIntoExistence):
    """
Scope note:
This property associates the instance of E66 Formation with the instance of E74 Group that it founded.


Examples:
- the formation of the CIDOC CRM SIG at the August 2000 CIDOC Board meeting (E66) has formed the CIDOC CRM Special Interest Group (E74)


In First Order Logic:
P95(x,y) &#8835; E66(x)
P95(x,y) &#8835; E74(y)
P95(x,y) &#8835; P92(x,y)
    """

    URI = "http://erlangen-crm.org/current/P95_has_formed"
