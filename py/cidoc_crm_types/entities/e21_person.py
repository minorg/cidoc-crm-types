from .e20_biological_object import E20BiologicalObject
from .e39_actor import E39Actor
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E21Person(E39Actor, E20BiologicalObject):
    """
Scope note:
This class comprises real persons who live or are assumed to have lived.

Legendary figures that may have existed, such as Ulysses and King Arthur, fall into this class if the documentation refers to them as historical figures. In cases where doubt exists as to whether several persons are in fact identical, multiple instances can be created and linked to indicate their relationship. The CIDOC CRM does not propose a specific form to support reasoning about possible identity.

In a bibliographic context, a name presented following the conventions usually employed for personal names will be assumed to correspond to an actual real person (an instance of E21 Person), unless evidence is available to indicate that this is not the case. The fact that a persona may erroneously be classified as an instance of E21 Person does not imply that the concept comprises personae.


Examples:
- Tut-Ankh-Amun (Edwards, 1979)
- Nelson Mandela (Brown, 2006)


In First Order Logic:
E21(x) ? E20(x)
E21(x) ? E39(x)
    """

    P152_has_parent: Tuple[object, ...] = ()  # Range: E21Person
    P152_is_parent_of: Tuple[object, ...] = ()  # Range: E21Person
    P97_was_father_for: Tuple[object, ...] = ()  # Range: E67Birth
    _typename: str = 'E21Person'
