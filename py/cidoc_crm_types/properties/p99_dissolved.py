from .p11_had_participant import P11HadParticipant
from .p93_took_out_of_existence import P93TookOutOfExistence
from dataclasses import dataclass


@dataclass
class P99Dissolved(P11HadParticipant, P93TookOutOfExistence):
    """
Scope note:
This property associates the instance of E68 Dissolution with the instance of E74 Group that it disbanded.


Examples:
- the end of The Hole in the Wall Gang (E68) dissolved The Hole in the Wall Gang (E74)


In First Order Logic:
P99(x,y) &#8835; E68(x)
P99(x,y) &#8835; E74(y)
P99(x,y) &#8835; P11(x,y)
P99(x,y) &#8835; P93(x,y)
    """

    URI = "http://erlangen-crm.org/current/P99_dissolved"
