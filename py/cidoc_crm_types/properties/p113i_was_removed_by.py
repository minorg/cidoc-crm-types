from .p12i_was_present_at import P12iWasPresentAt
from dataclasses import dataclass


@dataclass
class P113iWasRemovedBy(P12iWasPresentAt):
    URI = "http://erlangen-crm.org/current/P113i_was_removed_by"
