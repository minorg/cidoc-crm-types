from .p16i_was_used_for import P16iWasUsedFor
from dataclasses import dataclass


@dataclass
class P111iWasAddedBy(P16iWasUsedFor):
    URI = "http://erlangen-crm.org/current/P111i_was_added_by"
