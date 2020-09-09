from .e64_end_of_existence import E64EndofExistence
from dataclasses import dataclass


@dataclass
class E68Dissolution(E64EndofExistence):
    """
Scope note:
This class comprises the events that result in the formal or informal termination of an instance of E74 Group.

If the dissolution was deliberate, the Dissolution event should also be instantiated as an instance of E7 Activity.


Examples:
- the fall of the Roman Empire (Whittington, 1964)
- the liquidation of Enron Corporation (Atlas, 2001)


In First Order Logic:
E68(x) &#8835; E64(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E68_Dissolution"
