from dataclasses import dataclass


@dataclass
class P44HasCondition:
    """
Scope note:
This property records an E3 Condition State for some E18 Physical Thing.
It is a shortcut of the more fully developed path from &#8216;E18 Physical Thing&#8217; through &#8216;P34 concerned&#8217;, &#8216;E14 Condition Assessment&#8217;, &#8216;P35 has identified&#8217;, to &#8216;E3 Condition State&#8217;. It offers no information about how and when the E3 Condition State was established, nor by whom.

An instance of Condition State is specific to an instance of Physical Thing.


Examples:
- silver cup 232 (E22) has condition oxidation traces were present in 1997 (E3) has type oxidation traces (E55)


In First Order Logic:
P44(x,y) &#8835; E18(x)
P44(x,y) &#8835; E3(y)
    """

    URI = "http://erlangen-crm.org/current/P44_has_condition"
