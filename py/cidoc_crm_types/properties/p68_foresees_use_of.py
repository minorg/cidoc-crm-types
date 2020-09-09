from .p67_refers_to import P67RefersTo
from dataclasses import dataclass


@dataclass
class P68ForeseesUseOf(P67RefersTo):
    """
Scope note:
This property identifies an instance of E57 Material foreseen to be used by an instance of E29 Design or Procedure.

E29 Designs and procedures commonly foresee the use of particular instances of E57 Material. The fabrication of adobe bricks, for example, requires straw, clay and water. This property enables this to be documented.

This property is not intended for the documentation of instances of E57 Materials that were used on a particular occasion when an instance of E29 Design or Procedure was executed.


Examples:
- procedure for soda glass manufacture (E29) foresees use of soda (E57)


In First Order Logic:
P68(x,y) &#8835; E29(x)
P68(x,y) &#8835; E57(y)
P68(x,y) &#8835; P67(x,y)
    """

    URI = "http://erlangen-crm.org/current/P68_foresees_use_of"
