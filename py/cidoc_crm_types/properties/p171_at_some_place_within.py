from dataclasses import dataclass


@dataclass
class P171AtSomePlaceWithin:
    """
Scope note:
This property describes the maximum spatial extent within which an instance of E53 Place falls. Since instances of E53 Places may not have precisely known spatial extents, the CIDOC CRM supports statements about maximum spatial extents of instances of E53 Place. This property allows an instance of an instance of E53 Places&#8217;s maximum spatial extent (i.e. its outer boundary) to be assigned an instance of E94 Space Primitive value.

P171 at some place within is a shortcut of the fully developed path E53 Place, P89 falls within, E53 Place, P168 place is defined by, E94 Space Primitive through a declarative Place that is not explicitly documented, to a Space Primitive: declarative places are defined in CRMgeo (Doerr and Hiebel 2013).


Examples:	
- the spatial extent of the Acropolis of Athens (E53) is at some place within POLYGON ((37.969172 23.720787, 37.973122 23.721495 37.972741 23.728994, 37.969299 23.729735, 37.969172 23.720787)) (E94)


In First Order Logic:
P171(x,y) &#8835; E53(x)
P171(x,y) &#8835; E94(y)
    """

    URI = "http://erlangen-crm.org/current/P171_at_some_place_within"
