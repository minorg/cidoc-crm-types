from .p31_has_modified import P31HasModified
from dataclasses import dataclass


@dataclass
class P112Diminished(P31HasModified):
    """
Scope note:
This property identifies the instance E24 Physical Human-Made Thing that was diminished by an instance of E80 Part Removal.

Although an instance of E80 Part removal activity normally concerns only one instance of E24 Physical Human-Made Thing, it is possible to imagine circumstances under which more than one item might be diminished by a single instance of E80 Part Removal activity. 


Examples:
- the coffin of Tut-Ankh-Amun (E22) was diminished by The opening of the coffin of Tut-Ankh-Amun (E80)


In First Order Logic:
P112(x,y) &#8835; E80(x)
P112(x,y) &#8835; E24(y)
P112(x,y) &#8835; P31(x,y)
    """

    URI = "http://erlangen-crm.org/current/P112_diminished"
