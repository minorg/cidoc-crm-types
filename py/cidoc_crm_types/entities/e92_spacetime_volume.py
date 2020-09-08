from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E92SpacetimeVolume(E1CRMEntity):
    P10_contains: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P10_falls_within: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P132_overlaps_with: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P133_is_separated_from: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P160_has_temporal_projection: Tuple[object, ...] = ()  # Range: E52TimeSpan
    P161_has_spatial_projection: Tuple[object, ...] = ()  # Range: E53Place
    P166i_had_presence: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P169i_spacetime_volume_is_defined_by: Tuple[object, ...] = ()  # Range: object
    P196i_is_defined_by: Tuple[object, ...] = ()  # Range: E18PhysicalThing
