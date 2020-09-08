from .e92_spacetime_volume import E92SpacetimeVolume
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E93SpacetimeSnapshot(E92SpacetimeVolume):
    """
Scope note: 
This class comprises instances of E92 Spacetime Volume, whose temporal extent has been chosen in order to determine the spatial extent of a phenomenon over the chosen time-span. Respective phenomena may, for instance, be historical events or periods, but can also be the diachronic extent and existence of physical things. In other words, instances of this class fix a slice of another instance of E92 Spacetime Volume in time.

The temporal extent of an instance of E93 Presence typically is predetermined by the researcher so as to focus the investigation particularly on finding the spatial extent of the phenomenon by testing for its characteristic features. There are at least two basic directions such investigations might take. The investigation may wish to determine where something was during some time or it may wish to reconstruct the total passage of a phenomenon?s spacetime volume through an examination of discrete presences. Observation and measurement of features indicating the presence or absence of a phenomenon in some space allows for the progressive approximation of spatial extents through argumentation typically based on inclusion, exclusion and various overlaps.


In First Order Logic:
E93(x) ? E92(x)
    """

    P167_at: Tuple[object, ...] = ()  # Range: E53Place
    P195_was_presence_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    __typename: str = 'E93SpacetimeSnapshot'
