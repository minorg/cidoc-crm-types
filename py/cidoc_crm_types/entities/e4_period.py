from dataclasses import dataclass
from .e92_spacetime_volume import E92SpacetimeVolume
from .e2_temporal_entity import E2TemporalEntity


@dataclass
class E4Period(E92SpacetimeVolume, E2TemporalEntity):
    pass
