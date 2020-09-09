from .p140_assigned_attribute_to import P140AssignedAttributeTo
from dataclasses import dataclass


@dataclass
class P41Classified(P140AssignedAttributeTo):
    """
Scope note:
This property records the item to which a type was assigned in an E17 Type Assignment activity.
Any instance of a CIDOC CRM entity may be assigned a type through type assignment. Type assignment events allow a more detailed path from &#8216;E1 CRM Entity&#8217; through &#8216;P41i was classified by&#8217;, &#8216;E17 Type Assignment&#8217;, &#8216;P42 assigned&#8217;, to &#8216;E55 Type&#8217; for assigning types to objects compared to the shortcut offered by P2 has type (is type of).


Examples:
- 31 August 1997 classification of silver cup 232 (E17) classified silver cup 232 (E22)


In First Order Logic:
P41(x,y) &#8835; E17(x)
P41(x,y) &#8835; E1(y)
P41(x,y) &#8835; P140(x,y)
    """

    URI = "http://erlangen-crm.org/current/P41_classified"
