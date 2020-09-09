from .p14_carried_out_by import P14CarriedOutBy
from dataclasses import dataclass


@dataclass
class P22TransferredTitleTo(P14CarriedOutBy):
    """
Scope note:
This property identifies the instance of E39 Actor that acquires the legal ownership of an object as a result of an instance of E8 Acquisition.

The property will typically describe an Actor purchasing or otherwise acquiring an object from another Actor. However, title may also be acquired, without any corresponding loss of title by another Actor, through legal fieldwork such as hunting, shooting or fishing.

In reality the title is either transferred to or from someone, or both.


Examples:
- acquisition of the Amoudrouz collection by the Geneva Ethnography Museum (E8) transferred title to Geneva Ethnography Museum (E74)


In First Order Logic:
P22(x,y) &#8835; E8(x)
P22(x,y) &#8835; E39(y)
P22 (x,y) &#8835; P14(x,y)
    """

    URI = "http://erlangen-crm.org/current/P22_transferred_title_to"
