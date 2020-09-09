from dataclasses import dataclass


@dataclass
class P30TransferredCustodyOf:
    """
Scope note:
This property identifies the instance(s) of E18 Physical Thing concerned in an instance of E10 Transfer of Custody.

The property will typically describe the object that is handed over by an instance of E39 Actor to to the custody of another instance of E39 Actor. On occasion, physical custody may be transferred involuntarily or illegally &#8211; through accident, unsolicited donation, or theft.


Examples:
- the delivery of the paintings by Secure Deliveries Inc. to the National Gallery (E10) transferred custody of paintings from The Iveagh Bequest (E19)


In First Order Logic:
P30 (x,y) &#8835; E10(x)
P30 (x,y) &#8835; E18(y)
    """

    URI = "http://erlangen-crm.org/current/P30_transferred_custody_of"
