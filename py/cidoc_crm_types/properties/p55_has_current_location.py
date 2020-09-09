from .p53_has_former_or_current_location import P53HasFormerOrCurrentLocation
from dataclasses import dataclass


@dataclass
class P55HasCurrentLocation(P53HasFormerOrCurrentLocation):
    """
Scope note:
This property records the location of an instance of E19 Physical Object at the time of validity of the record or database containing the statement that uses this property.

This property is a specialisation of P53 has former or current location (is former or current location of).
It indicates that the instance of E53 Place associated with the instance of E19 Physical Object is the current location of the object. The property does not allow any indication of how long the object has been at the current location.

P55 has current location (currently holds) is a shortcut. A more detailed representation can make use of the fully developed (i.e. indirect) path from &#8216;E19 Physical Object&#8217;,through, &#8216;P25i moved by&#8217;, &#8216;E9 Move&#8217;, &#8216;P26 moved to&#8217;, to, &#8216;E53 Place&#8217;if and only if this Move is the most recent.


Examples:
- silver cup 232 (E22) has current location Display cabinet 23, Room 4, British Museum (E53)


In First Order Logic:
P55(x,y) &#8835; E19(x)
P55(x,y) &#8835; E53(y)
P55(x,y) &#8835; P53(x,y)
    """

    URI = "http://erlangen-crm.org/current/P55_has_current_location"
