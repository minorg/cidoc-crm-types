from .p140_assigned_attribute_to import P140AssignedAttributeTo
from dataclasses import dataclass


@dataclass
class P34Concerned(P140AssignedAttributeTo):
    """
Scope note:
This property identifies the instance of E18 Physical Thing that was assessed during an instance of E14 Condition Assessment activity.
Conditions may be assessed either by direct observation or using recorded evidence. In the latter case the instance of E18 Physical Thing does not need to be present or extant at the time of assessment.


Examples:
- 1997 condition assessment of the silver collection (E14) concerned silver cup 232 (E22)


In First Order Logic:
P34(x,y) &#8835; E14(x)
P34(x,y) &#8835; E18(y)
P34(x,y) &#8835; P140(x,y)
    """

    URI = "http://erlangen-crm.org/current/P34_concerned"
