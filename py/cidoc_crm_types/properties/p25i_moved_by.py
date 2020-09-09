from .p12i_was_present_at import P12iWasPresentAt
from dataclasses import dataclass


@dataclass
class P25iMovedBy(P12iWasPresentAt):
    URI = "http://erlangen-crm.org/current/P25i_moved_by"
