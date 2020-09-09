from .p14_carried_out_by import P14CarriedOutBy
from dataclasses import dataclass


@dataclass
class P23TransferredTitleFrom(P14CarriedOutBy):
    """
Scope note:
This property identifies the E39 Actor or Actors who relinquish legal ownership as the result of an E8 Acquisition.

The property will typically be used to describe a person donating or selling an object to a museum. In reality title is either transferred to or from someone, or both.


Examples:
- acquisition of the Amoudrouz collection by the Geneva Ethnographic Museum (E8) transferred title from Heirs of Amoudrouz (E74)


In First Order Logic:
P23(x,y) &#8835; E8(x)
P23(x,y) &#8835; E39(y)
P23 (x,y) &#8835; P14(x,y)
    """

    URI = "http://erlangen-crm.org/current/P23_transferred_title_from"
