from .p141i_was_assigned_by import P141iWasAssignedBy
from dataclasses import dataclass


@dataclass
class P42iWasAssignedBy(P141iWasAssignedBy):
    URI = "http://erlangen-crm.org/current/P42i_was_assigned_by"
