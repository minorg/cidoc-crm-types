from .p14_carried_out_by import P14CarriedOutBy
from dataclasses import dataclass


@dataclass
class P29CustodyReceivedBy(P14CarriedOutBy):
    """
Scope note:
This property identifies the instance(s) E39 Actor who receive custody of an instance of E18 Physical Thing in an instance of E10 Transfer of Custody.

The property will typically describe Actors receiving custody of an object when it is handed over from Definition of the CIDOC Conceptual Reference Model version 6.2.8 58 another Actor&#8217;s care. On occasion, physical custody may be received involuntarily or illegally &#8211; through accident, unsolicited donation, or theft.
In reality, custody is either transferred to someone or from someone, or both.


Examples:
- representatives of The National Gallery (E74) received custody through. The delivery of the paintings by Secure Delivieries Inc. to the National Gallery (E10)


In First Order Logic:
P29 (x,y) &#8835; E10(x)
P29 (x,y) &#8835; E39(y)
P29(x,y) &#8835; P14(x,y)
    """

    URI = "http://erlangen-crm.org/current/P29_custody_received_by"
