from .p16i_was_used_for import P16iWasUsedFor
from dataclasses import dataclass


@dataclass
class P142iWasUsedIn(P16iWasUsedFor):
    URI = "http://erlangen-crm.org/current/P142i_was_used_in"
