from dataclasses import dataclass


@dataclass
class P172Contains:
    """
Scope note:
This property describes a minimum spatial extent which is contained within an instance of E53 Place.
Since instances of E53 Place may not have precisely known spatial extents, the CIDOC CRM supports statements about minimum spatial extents of instances of E53 Place. This property allows an instance of E53 Places&#8217;s minimum spatial extent (i.e. its inner boundary or a point being within a Place) to be assigned an instance of E94 Space Primitive value.
This property is a shortcut of the fully developed path: E53 Place, P89i contains, E53 Place, P168 place is defined by, E94 Space Primitive


Examples:	
- the spatial extent of the Acropolis of Athens (E53) contains POINT (37.971431 23.725947) (E94)


In First Order Logic:
P172(x,y) &#8835; E53(x)
P172(x,y) &#8835; E94(y)
    """

    URI = "http://erlangen-crm.org/current/P172_contains"
