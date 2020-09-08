from .e92_spacetime_volume import E92SpacetimeVolume
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E93SpacetimeSnapshot(E92SpacetimeVolume):
    P167_at: Tuple[object, ...] = ()  # Range: E53Place
    P195_was_presence_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
