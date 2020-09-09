from .e7_activity import E7Activity
from dataclasses import dataclass


@dataclass
class E9Move(E7Activity):
    """
Scope note:
This class comprises changes of the physical location of the instances of E19 Physical Object.

Note, that the class E9 Move inherits the property P7 took place at (witnessed): E53 Place. This property should be used to describe the trajectory or a larger area within which a move takes place, whereas the properties P26 moved to (was destination of), P27 moved from (was origin of) describe the start and end points only. Moves may also be documented to consist of other moves (via P9 consists of (forms part of)), in order to describe intermediate stages on a trajectory. In that case, start and end points of the partial moves should match appropriately between each other and with the overall event.


Examples:
- the relocation of London Bridge from the UK to the USA. (Clarke, 1992)
- the movement of the exhibition &#8220;Treasures of Tut-Ankh-Amun&#8221; 1976-1979 (Treasures of Tutankhamun, exhibition catalogue, 1972) .


In First Order Logic:
E9(x) &#8835; E7(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E9_Move"
