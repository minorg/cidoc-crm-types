from .p184i_ends_with_or_after_the_end_of import P184iEndsWithOrAfterTheEndOf
from dataclasses import dataclass


@dataclass
class P185iEndsAfterTheEndOf(P184iEndsWithOrAfterTheEndOf):
    URI = "http://erlangen-crm.org/current/P185i_ends_after_the_end_of"
