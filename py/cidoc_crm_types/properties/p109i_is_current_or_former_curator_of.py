from .p49i_is_former_or_current_keeper_of import P49iIsFormerOrCurrentKeeperOf
from dataclasses import dataclass


@dataclass
class P109iIsCurrentOrFormerCuratorOf(P49iIsFormerOrCurrentKeeperOf):
    URI = "http://erlangen-crm.org/current/P109i_is_current_or_former_curator_of"
