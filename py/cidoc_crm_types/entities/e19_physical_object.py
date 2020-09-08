from .e18_physical_thing import E18PhysicalThing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E19PhysicalObject(E18PhysicalThing):
    P188i_is_production_tool_for: Tuple[object, ...] = ()  # Range: E99ProductType
    P54_has_current_permanent_location: Tuple[object, ...] = ()  # Range: E53Place
    P57_has_number_of_parts: Tuple[object, ...] = ()  # Range: object
