from .p175i_starts_after_or_with_the_start_of import P175iStartsAfterOrWithTheStartOf
from dataclasses import dataclass


@dataclass
class P176iStartsAfterTheStartOf(P175iStartsAfterOrWithTheStartOf):
    URI = "http://erlangen-crm.org/current/P176i_starts_after_the_start_of"
