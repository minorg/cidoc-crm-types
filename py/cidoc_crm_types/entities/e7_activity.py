from .e5_event import E5Event
from dataclasses import dataclass


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
- the writing of &#8220;Faust&#8221; by Goethe (E65) (Williams, 1987)
- the formation of the Bauhaus 1919 (E66) (Droste, 2006)
- calling the place identified by TGN &#8216;7017998&#8217; &#8216;Quyunjig&#8217; by the people of Iraq
- Kira Weber working in glass art from 1984 to 1993
- Kira Weber working in oil and pastel painting from 1993


In First Order Logic:
E7(x) &#8835; E5(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E7_Activity"
