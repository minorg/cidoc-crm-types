from .e5_event import E5Event
from dataclasses import dataclass


@dataclass
class E64EndofExistence(E5Event):
    """
Scope note:
This class comprises events that end the existence of any instance of E77 Persistent Item.

It may be used for temporal reasoning about things (physical items, groups of people, living beings) ceasing to exist; it serves as a hook for determination of a ?terminus post quem? or ?terminus ante quem?. In cases where substance from an instance of E64 Persistent Item continues to exist in a new form, the process would be documented as instances of E81 Transformation.


Examples:
- the death of Snoopy, my dog
- the melting of the snowmanthe burning of the Temple of Artemis in Ephesos by Herostratos in 356BC (Trell, 1945)


In First Order Logic:
E64(x) ? E5(x)
    """

    _typename: str = 'E64EndofExistence'
