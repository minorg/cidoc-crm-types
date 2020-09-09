from .p46i_forms_part_of import P46iFormsPartOf
from dataclasses import dataclass


@dataclass
class P56iIsFoundOn(P46iFormsPartOf):
    URI = "http://erlangen-crm.org/current/P56i_is_found_on"
