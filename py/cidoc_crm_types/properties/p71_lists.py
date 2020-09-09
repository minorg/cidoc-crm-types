from .p67_refers_to import P67RefersTo
from dataclasses import dataclass


@dataclass
class P71Lists(P67RefersTo):
    """
Scope note:
This property associates an instance of E32 Authority Document, with an instance of E1 CRM Entity which
it lists for reference purposes.


Examples:
- the Art & Architecture Thesaurus (E32) lists alcazars (E55)


In First Order Logic:
P71(x,y) &#8835; E32(x)
P71(x,y) &#8835; E1(y)
P71(x,y) &#8835; P67(x,y)
    """

    URI = "http://erlangen-crm.org/current/P71_lists"
