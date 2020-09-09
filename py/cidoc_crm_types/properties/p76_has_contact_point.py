from dataclasses import dataclass


@dataclass
class P76HasContactPoint:
    """
Scope note:
This property associates an instance of E39 Actor to an instance of E41 Appellation which a communication service uses to direct communications to this actor, such as an e-mail address, fax number, or postal address.

Examples:
- RLG (E40) has contact point "bl.ric@rlg.org" (E41)

In First Order Logic:
P76(x,y) &#8835; E39(x)
P76(x,y) &#8835; E41(y)
    """

    URI = "http://erlangen-crm.org/current/P76_has_contact_point"
