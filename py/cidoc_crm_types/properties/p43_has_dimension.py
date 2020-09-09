from dataclasses import dataclass


@dataclass
class P43HasDimension:
    """
Scope note:
This property records a E54 Dimension of some E70 Thing.
It is a shortcut of the more fully developed path from &#8216;E70 Thing&#8217; through &#8216;P39 measured&#8217;, &#8216;E16 Measurement&#8217;, &#8216;P40 observed dimension&#8217;, to &#8216;E54 Dimension&#8217;. It offers no information about how and when an E54 Dimension was established, nor by whom.

An instance of E54 Dimension is specific to an instance of E70 Thing.


Examples:
- silver cup 232 (E22) has dimension height of silver cup 232 (E54) has unit (P91) mm (E58), has value (P90) 224 (E60)


In First Order Logic:
P43(x,y) &#8835; E70(x)
P43(x,y) &#8835; E54(y)
    """

    URI = "http://erlangen-crm.org/current/P43_has_dimension"
