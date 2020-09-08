from .e77_persistent_item import E77PersistentItem
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E70Thing(E77PersistentItem):
    P101_had_as_general_use: Tuple[object, ...] = ()  # Range: E55Type
    P130_features_are_also_found_on: Tuple[object, ...] = ()  # Range: E70Thing
    P130_shows_features_of: Tuple[object, ...] = ()  # Range: E70Thing
    P43_has_dimension: Tuple[object, ...] = ()  # Range: E54Dimension
