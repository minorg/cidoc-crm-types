from .p91_has_unit import P91HasUnit
from dataclasses import dataclass


@dataclass
class P180HasCurrency(P91HasUnit):
    """
Scope note:
This property establishes the relationship between an instance of E97 Monetary Amount and the instance of E98 Currency that it is measured in.


Examples:	
- Christies&#8217; hammer price for &#8220;Vase with Fifteen Sunflowers&#8221; (E97) has currency British Pounds (E98)


In First Order Logic:
P180(x,y) &#8835; E97(x)
P180(x,y) &#8835; E98(y)
P180(x,y) &#8835; P91(x,y)
    """

    URI = "http://erlangen-crm.org/current/P180_has_currency"
