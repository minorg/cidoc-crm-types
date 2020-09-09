from .p14_carried_out_by import P14CarriedOutBy
from dataclasses import dataclass


@dataclass
class P28CustodySurrenderedBy(P14CarriedOutBy):
    """
Scope note:
This property identifies the instance(s) of E39 Actor who surrender custody of an instance of E18 Physical Thing in an instance of E10 Transfer of Custody.

The property will typically describe an Actor surrendering custody of an object when it is handed over to someone else&#8217;s care. On occasion, physical custody may be surrendered involuntarily &#8211; through accident, loss or theft.
In reality, custody is either transferred to someone or from someone, or both.

Examples:
- the Secure Deliveries Inc. crew (E74) surrendered custody through The delivery of the paintings by Secure Deliveries Inc. to the National Gallery (E10)

In First Order Logic:
P28(x,y) &#8835; E10(x)
P28(x,y) &#8835; E39(y)
P28(x,y) &#8835; P14(x,y)
    """

    URI = "http://erlangen-crm.org/current/P28_custody_surrendered_by"
