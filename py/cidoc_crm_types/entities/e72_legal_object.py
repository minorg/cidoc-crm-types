from .e70_thing import E70Thing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E72LegalObject(E70Thing):
    """
Scope note:
This class comprises those material or immaterial items to which instances of E30 Right, such as the right of ownership or use, can be applied.

This is true for all instances of E18 Physical Thing. In the case of instances of E28 Conceptual Object, however, the identity of an instance of E28 Conceptual Object or the method of its use may be too ambiguous to reliably establish instances of E30 Right, as in the case of taxa and inspirations. Ownership of corporations is currently regarded as out of scope of the CIDOC CRM.


Examples:
- the Cullinan diamond (E19) (Scarratt and Shor, 2006)
- definition of the CIDOC Conceptual Reference Model Version 5.0.4 (E73) (ISO 21127: 2004)


In First Order Logic:
E72(x) ? E70(x)
    """

    P104_is_subject_to: Tuple[object, ...] = ()  # Range: E30Right
    P105_right_held_by: Tuple[object, ...] = ()  # Range: E39Actor
    _typename: str = 'E72LegalObject'
