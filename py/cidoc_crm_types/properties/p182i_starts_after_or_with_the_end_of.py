from .p176i_starts_after_the_start_of import P176iStartsAfterTheStartOf
from .p185i_ends_after_the_end_of import P185iEndsAfterTheEndOf
from dataclasses import dataclass


@dataclass
class P182iStartsAfterOrWithTheEndOf(P176iStartsAfterTheStartOf, P185iEndsAfterTheEndOf):
    URI = "http://erlangen-crm.org/current/P182i_starts_after_or_with_the_end_of"
