from .e77_persistent_item import E77PersistentItem
from dataclasses import dataclass


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
E39(x) &#8835; E77(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E39_Actor"
