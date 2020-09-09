from dataclasses import dataclass


@dataclass
class P186ProducedThingOfProductType:
    """
Scope note:
This property associates an instance of E12 Production with the instance of E99 Production Type, that is, the type of the things it produces.


Examples: 	
- The production activity of the Volkswagen factory during 1949-1953 (E12) produced thing of product type Volkswagen Type 11 (Beetle) (E99).


In First Order Logic:
P186(x,y) &#8835; E12(x)
P186(x,y) &#8835; E99(y)
P186(x,y) &#8835; (&#8707;z)[E24(z) &#8743; P108(x,z) &#8743; P2(z,y)]
    """

    URI = "http://erlangen-crm.org/current/P186_produced_thing_of_product_type"
