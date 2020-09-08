from .e64_end_of_existence import E64EndofExistence
from dataclasses import dataclass


@dataclass
class E6Destruction(E64EndofExistence):
    """
Scope note:
This class comprises events that destroy one or more instances of E18 Physical Thing such that they lose their identity as the subjects of documentation.

Some destruction events are intentional, while others are independent of human activity. Intentional destruction may be documented by classifying the event as both an instance of E6 Destruction and of E7 Activity.

The decision to document an object as destroyed, transformed or modified is context sensitive:
1. If the matter remaining from the destruction is not documented, the event is modelled solely as an instance of E6 Destruction.
2. An event should also be documented as an instance of E81 Transformation if it results in the destruction of one or more objects and the simultaneous production of others using parts or material from the original. In this case, the new items have separate identities. Matter is preserved, but identity is not.
3. When the initial identity of the changed instance of E18 Physical Thing is preserved, the event should be documented as an instance of E11 Modification.


Examples:
- the destruction of Herculaneum by volcanic eruption in 79 AD (Camardo, 2013)
- the destruction of Nineveh (E6, E7) (George, 2000)
- the breaking of a champagne glass yesterday by my dog


In First Order Logic:
E6(x) ? E64(x)
    """

    __typename: str = 'E6Destruction'
