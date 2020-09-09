from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass


@dataclass
class E53Place(E1CRMEntity):
    """
Scope note:
This class comprises extents in space, in particular on the surface of the earth, in the pure sense of physics: independent from temporal phenomena and matter.

The instances of E53 Place are usually determined by reference to the position of &#8220;immobile&#8221; objects such as buildings, cities, mountains, rivers, or dedicated geodetic marks, but may also be determined by reference to mobile objetcts. A Place can be determined by combining a frame of reference and a location with respect to this frame.

It is sometimes argued that instances of E53 Place are best identified by global coordinates or absolute reference systems. However, relative references are often more relevant in the context of cultural documentation and tend to be more precise. In particular, we are often interested in position in relation to large, mobile objects, such as ships. For example, the Place at which Nelson died is known with reference to a large mobile object &#8211; H.M.S Victory. A resolution of this Place in terms of absolute coordinates would require knowledge of the movements of the vessel and the precise time of death, either of which may be revised, and the result would lack historical and cultural relevance. 

Any instance of E18 Physical Thing can serve as a frame of reference for an instance of E53 Place. This may be documented using the property P157 is at rest relative to (provides reference space for).


Examples:
- the extent of the UK in the year 2003
- the position of the hallmark on the inside of my wedding ring
- the place referred to in the phrase: "Fish collected at three miles north of the confluence of the Arve and the Rhone"
- here -> <-


In First Order Logic:
E53(x) &#8835; E1(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E53_Place"
