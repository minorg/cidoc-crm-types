from dataclasses import dataclass


@dataclass
class P53HasFormerOrCurrentLocation:
    """
Scope note:
This property identifies an instance of E53 Place as the former or current location of an instance of E18 Physical Thing.

In the case of instances of E19 Physical Object, the property does not allow any indication of the TimeSpan during which the instance of E19 Physical Object was located at this instance of E53 Place, nor if this is the current location.

In the case of immobile objects, the Place would normally correspond to the Place of creation. 
P53 has former or current location (is former or current location of) is a shortcut. A more detailed representation can make use of the fully developed (i.e. indirect) path from &#8216;E19 Physical Object&#8217;, though, &#8216;P25i moved by&#8217;, &#8216;E9 Move&#8217;, &#8216;P26 moved to&#8217; or &#8216;P27 moved from&#8217;, to &#8216; E53 Place&#8217;. 


Examples:
- silver cup 232 (E22) has former or current location Display Case 4, Room 23, Museum of Oxford (E53)


In First Order Logic:
P53(x,y) &#8835; E18(x)
P53(x,y) &#8835; E53(y)
    """

    URI = "http://erlangen-crm.org/current/P53_has_former_or_current_location"
