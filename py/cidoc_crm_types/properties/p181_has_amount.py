from .p90_has_value import P90HasValue
from dataclasses import dataclass


@dataclass
class P181HasAmount(P90HasValue):
    """
Scope note:
This property establishes the relationship between an instance of E97 Monetary Amount and the amount of currency, an instance of E60 Number, that it consists of.


Examples:	
- Christies hammer price for &#8220;Vase with Fifteen Sunflowers&#8221; (E97) has amount 24,750,000 (E60)


In First Order Logic:
P181(x,y) &#8835; E97(x)
P181(x,y) &#8835; E60(y)
P181(x,y) &#8835; P90(x,y)
    """

    URI = "http://erlangen-crm.org/current/P181_has_amount"
