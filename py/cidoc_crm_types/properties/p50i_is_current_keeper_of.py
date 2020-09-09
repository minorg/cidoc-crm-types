from .p49i_is_former_or_current_keeper_of import P49iIsFormerOrCurrentKeeperOf
from dataclasses import dataclass


@dataclass
class P50iIsCurrentKeeperOf(P49iIsFormerOrCurrentKeeperOf):
    URI = "http://erlangen-crm.org/current/P50i_is_current_keeper_of"
