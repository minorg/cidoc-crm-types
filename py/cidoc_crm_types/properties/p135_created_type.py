from .p94_has_created import P94HasCreated
from dataclasses import dataclass


@dataclass
class P135CreatedType(P94HasCreated):
    """
Scope note:
This property identifies the instance of E55 Type, which is created in an instance of E83 Type Creation


Examples:
- The description of a new ribbon worm species by B&#252;rger (E83) created type 'Lineus coxinus (B&#252;rger, 1892)' (E55)


In First Order Logic:
P135(x,y) &#8835; E83(x)
P135(x,y) &#8835; E55(y)
P135(x,y) &#8835; P94(x,y)
    """

    URI = "http://erlangen-crm.org/current/P135_created_type"
