from .p67_refers_to import P67RefersTo
from dataclasses import dataclass


@dataclass
class P129IsAbout(P67RefersTo):
    """
Scope note:
This property documents that an instance of E89 Propositional Object has as subject an instance of E1 CRM Entity.

This differs from P67 refers to (is referred to by), which refers to an instance of E1 CRM Entity, in that it describes the primary subject or subjects of an instance of E89 Propositional Object.


Examples:
- The text entitled 'Reach for the sky' (E33) is about Douglas Bader (E21)


In First Order Logic:
P129(x,y) &#8835; E89(x)
P129(x,y) &#8835; E1(y)
P129(x,y) &#8835; P67(x,y)
    """

    URI = "http://erlangen-crm.org/current/P129_is_about"
