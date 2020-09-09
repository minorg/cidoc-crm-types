from .p140_assigned_attribute_to import P140AssignedAttributeTo
from dataclasses import dataclass


@dataclass
class P39Measured(P140AssignedAttributeTo):
    """
Scope note:
This property associates an instance of E16 Measurement with the instance of E1 CRM Entity to which it applied. An instance of E1 CRM Entity may be measured more than once. Material and immaterial things and processes may be measured, e.g. the number of words in a text, or the duration of an event.


Examples:
- 31 August 1997 measurement of height of silver cup 232 (E16) measured silver cup 232 (E22)


In First Order Logic:
P39(x,y) &#8835; E16(x)
P39(x,y) &#8835; E1(y)
P39(x,y) &#8835; P140(x,y)
    """

    URI = "http://erlangen-crm.org/current/P39_measured"
