from .e41_appellation import E41Appellation
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E42Identifier(E41Appellation):
    P37_was_assigned_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P38_was_deassigned_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
