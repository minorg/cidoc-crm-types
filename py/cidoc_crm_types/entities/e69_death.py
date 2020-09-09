from .e64_end_of_existence import E64EndofExistence
from dataclasses import dataclass


@dataclass
class E69Death(E64EndofExistence):
    """
Scope note:
This class comprises the deaths of human beings.
If a person is killed, the death should be documented as an instance of both E69 Death and E7 Activity. The death or perishing of other living beings should be documented asinstances of E64 End of Existence.


Examples:
- the murder of Julius Caesar (E69,E7) (Irwin, 1935)
- the death of Senator Paul Wellstone (Monast, 2003)


In First Order Logic:
E69(x) &#8835; E64(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E69_Death"
