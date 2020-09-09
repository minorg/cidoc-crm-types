from dataclasses import dataclass


@dataclass
class P51HasFormerOrCurrentOwner:
    """
Scope note:
 This property identifies an instance of E39 Actor that is or had been the legal owner (i.e. title holder) of an instance of E18 Physical Thing at some time.

The distinction with P52 has current owner (is current owner of) is that P51 has former or current owner (is former or current owner of) does not indicate whether the specified owners are current. P51 has former or current owner (is former or current owner of) is a shortcut for the more detailed path from &#8216;E18 Physical Thing&#8217; through &#8216;P24i changed ownership through&#8217;, &#8216;E8 Acquisition&#8217;, &#8216;P23 transferred title from&#8217;, or &#8216;P22 transferred title to&#8217;,to &#8216;E39 Actor&#8217;.


Examples:
- paintings from the Iveagh Bequest (E18) has former or current owner Lord Iveagh (E21)


In First Order Logic:
P51(x,y) &#8835; E18(x)
P51(x,y) &#8835; E39(y)
    """

    URI = "http://erlangen-crm.org/current/P51_has_former_or_current_owner"
