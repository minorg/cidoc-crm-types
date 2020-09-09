from dataclasses import dataclass


@dataclass
class P24TransferredTitleOf:
    """
Scope note:
This property identifies the instance(s) of E18 Physical Thing involved in an instance of E8 Acquisition.

In reality, an acquisition must refer to at least one transferred item.


Examples:
- acquisition of the Amoudrouz collection by the Geneva Ethnographic Museum (E8) transferred title of Amoudrouz Collection (E78)


In First Order Logic:
P24(x,y) &#8835; E8(x)
P24(x,y) &#8835; E18(y)
    """

    URI = "http://erlangen-crm.org/current/P24_transferred_title_of"
