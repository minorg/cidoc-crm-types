from .p12_occurred_in_the_presence_of import P12OccurredInThePresenceOf
from dataclasses import dataclass


@dataclass
class P25Moved(P12OccurredInThePresenceOf):
    """
Scope note:
This property identifies an instance of E19 Physical Object that was moved by an instance of E9 Move. A move must concern at least one object.

The property implies the object&#8217;s passive participation. For example, Monet&#8217;s painting &#8220;Impression sunrise&#8221; was moved for the first Impressionist exhibition in 1874.


Examples:
- Monet&#180;s &#8220;Impression sunrise&#8221; (E22) moved by preparations for the First Impressionist Exhibition (E9)

In First Order Logic:
P25(x,y) &#8835; E9(x)
P25(x,y) &#8835; E19(y)
P25(x,y) &#8835; P12(x,y)
    """

    URI = "http://erlangen-crm.org/current/P25_moved"
