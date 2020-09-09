from .p173i_ends_with_or_after_the_start_of import P173iEndsWithOrAfterTheStartOf
from dataclasses import dataclass


@dataclass
class P174iEndsAfterTheStartOf(P173iEndsWithOrAfterTheStartOf):
    URI = "http://erlangen-crm.org/current/P174i_ends_after_the_start_of"
