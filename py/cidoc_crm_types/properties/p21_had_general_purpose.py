from dataclasses import dataclass


@dataclass
class P21HadGeneralPurpose:
    """
Scope note:
This property describes an intentional relationship between an E7 Activity and some general goal or purpose.

This may involve activities intended as preparation for some type of activity or event. P21 had general purpose (was purpose of) differs from P20 had specific purpose (was purpose of) in that no occurrence of an event is implied as the purpose.


Examples:
- Van Eyck's pigment grinding (E7) had general purpose painting (E55)
- the setting of trap 2742 on May 17th 1874 (E7) had general purpose Catching Moose (E55) (Activity type)


In First Order Logic:
P21(x,y) &#8835; E7(x)
P21(x,y) &#8835; E55(y)
    """

    URI = "http://erlangen-crm.org/current/P21_had_general_purpose"
