from .p93_took_out_of_existence import P93TookOutOfExistence
from dataclasses import dataclass


@dataclass
class P100WasDeathOf(P93TookOutOfExistence):
    """
Scope note:
This property links an E69 instance of E69 Death event to the instance of E21 Person that died.

An instance of E69 Death may involve multiple people, for example in the case of a battle or disaster.
This is not intended for use with general Natural History material, only people.


Examples:
- Mozart's death (E69) was death of Mozart (E21)

In First Order Logic:
P100(x,y) &#8835; E69(x)
P100(x,y) &#8835; E21(y)
P100(x,y) &#8835; P93(x,y)
    """

    URI = "http://erlangen-crm.org/current/P100_was_death_of"
