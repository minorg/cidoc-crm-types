from .e5_event import E5Event
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E7Activity(E5Event):
    """
Scope note:
This class comprises actions intentionally carried out by instances of E39 Actor that result in changes of state in the cultural, social, or physical systems documented.

This notion includes complex, composite and long-lasting actions such as the building of a settlement or a war, as well as simple, short-lived actions such as the opening of a door.


Examples:
- the Battle of Stalingrad (Hoyt, 1993)
- the Yalta Conference (Harbutt, 2010)
- my birthday celebration 28-6-1995
- the writing of ?Faust? by Goethe (E65) (Williams, 1987)
- the formation of the Bauhaus 1919 (E66) (Droste, 2006)
- calling the place identified by TGN ?7017998? ?Quyunjig? by the people of Iraq
- Kira Weber working in glass art from 1984 to 1993
- Kira Weber working in oil and pastel painting from 1993


In First Order Logic:
E7(x) ? E5(x)
    """

    P125_used_object_of_type: Tuple[object, ...] = ()  # Range: E55Type
    P15_was_influenced_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P17_was_motivated_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P19_was_intended_use_of: Tuple[object, ...] = ()  # Range: E71ManMadeThing
    P20_had_specific_purpose: Tuple[object, ...] = ()  # Range: E5Event
    P21_had_general_purpose: Tuple[object, ...] = ()  # Range: E55Type
    P32_used_general_technique: Tuple[object, ...] = ()  # Range: E55Type
    _typename: str = 'E7Activity'
