from .p174i_ends_after_the_start_of import P174iEndsAfterTheStartOf
from dataclasses import dataclass


@dataclass
class P184iEndsWithOrAfterTheEndOf(P174iEndsAfterTheStartOf):
    URI = "http://erlangen-crm.org/current/P184i_ends_with_or_after_the_end_of"
