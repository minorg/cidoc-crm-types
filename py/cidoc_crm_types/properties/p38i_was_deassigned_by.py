from .p141i_was_assigned_by import P141iWasAssignedBy
from dataclasses import dataclass


@dataclass
class P38iWasDeassignedBy(P141iWasAssignedBy):
    URI = "http://erlangen-crm.org/current/P38i_was_deassigned_by"
