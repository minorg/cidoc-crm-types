from .p141i_was_assigned_by import P141iWasAssignedBy
from dataclasses import dataclass


@dataclass
class P40iWasObservedIn(P141iWasAssignedBy):
    URI = "http://erlangen-crm.org/current/P40i_was_observed_in"
