from .e73_information_object import E73InformationObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E29DesignorProcedure(E73InformationObject):
    P187i_is_production_plan_for: Tuple[object, ...] = ()  # Range: E99ProductType
    P69_has_association_with: Tuple[object, ...] = ()  # Range: E29DesignorProcedure
    P69_is_associated_with: Tuple[object, ...] = ()  # Range: E29DesignorProcedure
