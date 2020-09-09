from .p132_spatiotemporally_overlaps_with import P132SpatiotemporallyOverlapsWith
from dataclasses import dataclass


@dataclass
class P9iFormsPartOf(P132SpatiotemporallyOverlapsWith):
    URI = "http://erlangen-crm.org/current/P9i_forms_part_of"
