from dataclasses import dataclass


@dataclass
class P49HasFormerOrCurrentKeeper:
    """
Scope note:
This property identifies the instance of E39 Actor who has or has had custody of an instance of E18 Physical Thing at some time. This property leaves open the question if parts of this physical thing have been added or removed during the time-spans it has been under the custody of this actor, but it is required that at least a part which can unambiguously be identified as representing the whole has been under this custody for its whole time. The way, in which a representative part is defined, should ensure that it is unambiguous who keeps a part and who the whole and should be consistent with the identity criteria of the kept instance of E18 Physical Thing.

The distinction with P50 has current keeper (is current keeper of) is that P49 has former or current keeper (is former or current keeper of) leaves open the question as to whether the specified keepers are current.

P49 has former or current keeper (is former or current keeper of) is a shortcut for the more detailed path from &#8216;E18 Physical Thing&#8217; through &#8216;P30 transferred custody of&#8217;, &#8216;E10 Transfer of Custody&#8217;, &#8216;P28 custody surrendered by&#8217; or &#8216;P29 custody received by&#8217; to &#8216; E39 Actor&#8217;.


Examples:
- paintings from The Iveagh Bequest (E18) has former or current keeper Secure Deliveries Inc. (E40)


In First Order Logic:
P49(x,y) &#8835; E18(x)
P49(x,y) &#8835; E39(y)
    """

    URI = "http://erlangen-crm.org/current/P49_has_former_or_current_keeper"
