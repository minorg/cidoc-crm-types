from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E13AttributeAssignment(E7Activity):
    P140_assigned_attribute_to: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P141_assigned: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P177_assigned_property_type: Tuple[object, ...] = ()  # Range: E55Type
