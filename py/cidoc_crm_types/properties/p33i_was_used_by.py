from .p16i_was_used_for import P16iWasUsedFor
from dataclasses import dataclass


@dataclass
class P33iWasUsedBy(P16iWasUsedFor):
    URI = "http://erlangen-crm.org/current/P33i_was_used_by"
