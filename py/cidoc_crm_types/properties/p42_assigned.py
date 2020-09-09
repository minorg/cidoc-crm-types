from .p141_assigned import P141Assigned
from dataclasses import dataclass


@dataclass
class P42Assigned(P141Assigned):
    """
Scope note:
This property records the type that was assigned to an entity by an E17 Type Assignment activity.
Type assignment events allow a more detailed path from &#8216;E1 CRM Entity&#8217; through &#8216;P41i was classified by&#8217;, &#8216;E17 Type Assignment&#8217;, &#8216;P42 assigned&#8217;, to &#8216;E55 Type&#8217; for assigning types to objects compared to the shortcut offered by P2 has type (is type of).
For example, a fragment of an antique vessel could be assigned the type &#8220;attic red figured belly handled amphora&#8221; by expert A. The same fragment could be assigned the type &#8220;shoulder handled amphora&#8221; by expert B.
A Type may be intellectually constructed independent from assigning an instance of it.


Examples:
- 31 August 1997 classification of silver cup 232 (E17) assigned goblet (E55)


In First Order Logic:
P42(x,y) &#8835; E17(x)
P42(x,y)&#8835; E55(y)
P42(x,y) &#8835; P141(x,y)
    """

    URI = "http://erlangen-crm.org/current/P42_assigned"
