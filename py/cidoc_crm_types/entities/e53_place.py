from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E53Place(E1CRMEntity):
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
