from .p141i_was_assigned_by import P141iWasAssignedBy
from dataclasses import dataclass


@dataclass
class P37iWasAssignedBy(P141iWasAssignedBy):
    URI = "http://erlangen-crm.org/current/P37i_was_assigned_by"
