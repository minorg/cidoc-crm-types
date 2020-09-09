from .p49_has_former_or_current_keeper import P49HasFormerOrCurrentKeeper
from dataclasses import dataclass


@dataclass
class P50HasCurrentKeeper(P49HasFormerOrCurrentKeeper):
    """
Scope note:
This property identifies the an instance of E39 Actor that had custody of an instance of E18 Physical Thing at the time of validity of the record or database containing the statement that uses this property.
P50 has current keeper (is current keeper of) is a shortcut for the more detailed path from &#8216;E18 Physical Thing&#8217; through, &#8216;P30i custody transferred through&#8217;, &#8216;E10 Transfer of Custody&#8217;, &#8216;P29 custody received by&#8217; ,to &#8216;E39 Actor&#8217;.


Examples:
- painting from The Iveagh Bequest (E18) has current keeper The National Gallery (E74)


In First Order Logic:
P50(x,y) &#8835; E18(x)
P50(x,y) &#8835; E39(y)
P50(x,y) &#8835; P49(x,y)
    """

    URI = "http://erlangen-crm.org/current/P50_has_current_keeper"
