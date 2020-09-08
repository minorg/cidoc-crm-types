from .e77_persistent_item import E77PersistentItem
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E39Actor(E77PersistentItem):
    """
Scope note:
This class comprises people, either individually or in groups, who have the potential to perform intentional actions of kinds for which someone may be held responsible.


Examples:
- London and Continental Railways (E40)
- the Governor of the Bank of England in 1975 (E21)
- Sir Ian McKellan (E21)


In First Order Logic:
E39(x) ? E77(x)
    """

    P105_has_right_on: Tuple[object, ...] = ()  # Range: E72LegalObject
    P107_is_current_or_former_member_of: Tuple[object, ...] = ()  # Range: E74Group
    P109_is_current_or_former_curator_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P49_is_former_or_current_keeper_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P50_is_current_keeper_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P51_is_former_or_current_owner_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P52_is_current_owner_of: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P74_has_current_or_former_residence: Tuple[object, ...] = ()  # Range: E53Place
    P75_possesses: Tuple[object, ...] = ()  # Range: E30Right
    P76_has_contact_point: Tuple[object, ...] = ()  # Range: E41Appellation
    __typename: str = 'E39Actor'
