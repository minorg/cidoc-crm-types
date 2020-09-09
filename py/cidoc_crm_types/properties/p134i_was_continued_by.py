from .p15i_influenced import P15iInfluenced
from .p174i_ends_after_the_start_of import P174iEndsAfterTheStartOf
from dataclasses import dataclass


@dataclass
class P134iWasContinuedBy(P174iEndsAfterTheStartOf, P15iInfluenced):
    URI = "http://erlangen-crm.org/current/P134i_was_continued_by"
