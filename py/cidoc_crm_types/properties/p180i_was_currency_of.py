from .p91i_is_unit_of import P91iIsUnitOf
from dataclasses import dataclass


@dataclass
class P180iWasCurrencyOf(P91iIsUnitOf):
    URI = "http://erlangen-crm.org/current/P180i_was_currency_of"
