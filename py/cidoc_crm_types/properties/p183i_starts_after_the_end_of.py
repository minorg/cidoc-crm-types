from .p182i_starts_after_or_with_the_end_of import P182iStartsAfterOrWithTheEndOf
from dataclasses import dataclass


@dataclass
class P183iStartsAfterTheEndOf(P182iStartsAfterOrWithTheEndOf):
    URI = "http://erlangen-crm.org/current/P183i_starts_after_the_end_of"
