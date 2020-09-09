from .p141i_was_assigned_by import P141iWasAssignedBy
from dataclasses import dataclass


@dataclass
class P35iWasIdentifiedBy(P141iWasAssignedBy):
    URI = "http://erlangen-crm.org/current/P35i_was_identified_by"
