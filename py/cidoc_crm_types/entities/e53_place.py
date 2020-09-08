from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E53Place(E1CRMEntity):
    """
Scope note:
This class comprises extents in space, in particular on the surface of the earth, in the pure sense of physics: independent from temporal phenomena and matter.

The instances of E53 Place are usually determined by reference to the position of ?immobile? objects such as buildings, cities, mountains, rivers, or dedicated geodetic marks, but may also be determined by reference to mobile objetcts. A Place can be determined by combining a frame of reference and a location with respect to this frame.

It is sometimes argued that instances of E53 Place are best identified by global coordinates or absolute reference systems. However, relative references are often more relevant in the context of cultural documentation and tend to be more precise. In particular, we are often interested in position in relation to large, mobile objects, such as ships. For example, the Place at which Nelson died is known with reference to a large mobile object ? H.M.S Victory. A resolution of this Place in terms of absolute coordinates would require knowledge of the movements of the vessel and the precise time of death, either of which may be revised, and the result would lack historical and cultural relevance. 

Any instance of E18 Physical Thing can serve as a frame of reference for an instance of E53 Place. This may be documented using the property P157 is at rest relative to (provides reference space for).


Examples:
- the extent of the UK in the year 2003
- the position of the hallmark on the inside of my wedding ring
- the place referred to in the phrase: "Fish collected at three miles north of the confluence of the Arve and the Rhone"
- here -> <-


In First Order Logic:
E53(x) ? E1(x)
    """

    P121_overlaps_with: Tuple[object, ...] = ()  # Range: E53Place
    P122_borders_with: Tuple[object, ...] = ()  # Range: E53Place
    P156i_is_occupied_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P157_is_at_rest_relative_to: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P161i_is_spatial_projection_of: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P167i_was_place_of: Tuple[object, ...] = ()  # Range: E93SpacetimeSnapshot
    P168_place_is_defined_by: Tuple[object, ...] = ()  # Range: object
    P171_at_some_place_within: Tuple[object, ...] = ()  # Range: object
    P172_contains: Tuple[object, ...] = ()  # Range: object
    P189_approximates: Tuple[object, ...] = ()  # Range: E53Place
    P189i_is_approximated_by: Tuple[object, ...] = ()  # Range: E53Place
    P26_was_destination_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P27_was_origin_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P53_is_former_or_current_location_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P54_is_current_permanent_location_of: Tuple[object, ...] = ()  # Range: E19PhysicalObject
    P55_currently_holds: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P59_is_located_on_or_within: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P74_is_current_or_former_residence_of: Tuple[object, ...] = ()  # Range: E39Actor
    P7_witnessed: Tuple[object, ...] = ()  # Range: E4Period
    P89_contains: Tuple[object, ...] = ()  # Range: E53Place
    P89_falls_within: Tuple[object, ...] = ()  # Range: E53Place
