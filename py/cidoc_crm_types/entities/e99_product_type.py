from .e55_type import E55Type
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E99ProductType(E55Type):
    P186_produced_thing_of_product_type: Tuple[object, ...] = ()  # Range: E12Production
    P187_has_production_plan: Tuple[object, ...] = ()  # Range: E29DesignorProcedure
    P188_requires_production_tool: Tuple[object, ...] = ()  # Range: E19PhysicalObject
