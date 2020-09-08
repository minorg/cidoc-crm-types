from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E92SpacetimeVolume(E1CRMEntity):
    """
Scope note:
This class comprises 4 dimensional point sets (volumes) in physical spacetime (in contrast to mathematical models of it) regardless their true geometric forms. They may derive their identity from being the extent of a material phenomenon or from being the interpretation of an expression defining an extent in spacetime. Intersections of instances of E92 Spacetime Volume, E53 Place and E52 Timespan are also regarded as instances of E92 Spacetime Volume. An instance of E92 Spacetime Volume is either contiguous or composed of a finite number of contiguous subsets. Its boundaries may be fuzzy due to the properties of the phenomena it derives from or due to the limited precision up to which defining expression can be identified with a real extent in spacetime. The duration of existence of an instance of E92 Spacetime Volume is its projection on time.


Examples:
- the?spacetime?Volume?of?the?Event?of?Ceasars?murder?
- the?spacetime?Volume?where?and?when?the?carbon?14?dating?of?the?"Schoeninger?Speer?II"?in?1996 ?took?place?
- the?spatio?temporal?trajectory?of?the?H.M.S.?Victory?from?its?building?to?its?actual?location
- the?spacetime?volume?defined?by?a?polygon?approximating?the?Danube?river?flood?in?Austria?between?6th?and?9th?of?August?2002


In First Order Logic:
E92(x) ? E1(x)
    """

    P10_contains: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P10_falls_within: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P132_overlaps_with: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P133_is_separated_from: Tuple[object, ...] = ()  # Range: E92SpacetimeVolume
    P160_has_temporal_projection: Tuple[object, ...] = ()  # Range: E52TimeSpan
    P161_has_spatial_projection: Tuple[object, ...] = ()  # Range: E53Place
    P166i_had_presence: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P169i_spacetime_volume_is_defined_by: Tuple[object, ...] = ()  # Range: object
    P196i_is_defined_by: Tuple[object, ...] = ()  # Range: E18PhysicalThing
