from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E9Move(E7Activity):
    """
Scope note:
This class comprises changes of the physical location of the instances of E19 Physical Object.

Note, that the class E9 Move inherits the property P7 took place at (witnessed): E53 Place. This property should be used to describe the trajectory or a larger area within which a move takes place, whereas the properties P26 moved to (was destination of), P27 moved from (was origin of) describe the start and end points only. Moves may also be documented to consist of other moves (via P9 consists of (forms part of)), in order to describe intermediate stages on a trajectory. In that case, start and end points of the partial moves should match appropriately between each other and with the overall event.


Examples:
- the relocation of London Bridge from the UK to the USA. (Clarke, 1992)
- the movement of the exhibition ?Treasures of Tut-Ankh-Amun? 1976-1979 (Treasures of Tutankhamun, exhibition catalogue, 1972) .


In First Order Logic:
E9(x) ? E7(x)
    """

    P26_moved_to: Tuple[object, ...] = ()  # Range: E53Place
    P27_moved_from: Tuple[object, ...] = ()  # Range: E53Place
    _typename: str = 'E9Move'
