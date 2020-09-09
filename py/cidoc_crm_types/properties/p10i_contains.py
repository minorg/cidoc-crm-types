from .p132_spatiotemporally_overlaps_with import P132SpatiotemporallyOverlapsWith
from dataclasses import dataclass


@dataclass
class P10iContains(P132SpatiotemporallyOverlapsWith):
    URI = "http://erlangen-crm.org/current/P10i_contains"
