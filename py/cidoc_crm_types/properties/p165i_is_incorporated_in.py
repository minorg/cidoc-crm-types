from .p106i_forms_part_of import P106iFormsPartOf
from dataclasses import dataclass


@dataclass
class P165iIsIncorporatedIn(P106iFormsPartOf):
    URI = "http://erlangen-crm.org/current/P165i_is_incorporated_in"
