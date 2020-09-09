from .p105i_has_right_on import P105iHasRightOn
from .p51i_is_former_or_current_owner_of import P51iIsFormerOrCurrentOwnerOf
from dataclasses import dataclass


@dataclass
class P52iIsCurrentOwnerOf(P51iIsFormerOrCurrentOwnerOf, P105iHasRightOn):
    URI = "http://erlangen-crm.org/current/P52i_is_current_owner_of"
