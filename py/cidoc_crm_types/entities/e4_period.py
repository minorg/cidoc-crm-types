from dataclasses import dataclass
from .e2_temporal_entity import E2TemporalEntity
from .e92_spacetime_volume import E92SpacetimeVolume


@dataclass
class E4Period(E2TemporalEntity, E92SpacetimeVolume):
    pass
