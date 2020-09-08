from .e2_temporal_entity import E2TemporalEntity
from .e92_spacetime_volume import E92SpacetimeVolume
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E4Period(E92SpacetimeVolume, E2TemporalEntity):
    P7_took_place_at: Tuple[object, ...] = ()  # Range: E53Place
    P8_took_place_on_or_within: Tuple[object, ...] = ()  # Range: E18PhysicalThing
