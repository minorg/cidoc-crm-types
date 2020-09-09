from .p174i_ends_after_the_start_of import P174iEndsAfterTheStartOf
from dataclasses import dataclass


@dataclass
class P175iStartsAfterOrWithTheStartOf(P174iEndsAfterTheStartOf):
    URI = "http://erlangen-crm.org/current/P175i_starts_after_or_with_the_start_of"
