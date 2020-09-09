from .p67i_is_referred_to_by import P67iIsReferredToBy
from dataclasses import dataclass


@dataclass
class P129iIsSubjectOf(P67iIsReferredToBy):
    URI = "http://erlangen-crm.org/current/P129i_is_subject_of"
