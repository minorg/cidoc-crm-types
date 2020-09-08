from .e28_conceptual_object import E28ConceptualObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E89PropositionalObject(E28ConceptualObject):
    """
Scope note:
This class comprises immaterial items, including but not limited to stories, plots, procedural prescriptions, algorithms, laws of physics or images that are, or represent in some sense, sets of propositions about real or imaginary things and that are documented as single units or serve as topic of discourse.

This class also comprises items that are ?about? something in the sense of a subject. In the wider sense, this class includes expressions of psychological value such as non-figural art and musical themes. However, conceptual items such as types and classes are not instances of E89 Propositional Object. This should not be confused with the definition of a type, which is indeed an instance of E89 Propositional Object.


Examples:
- Maxwell?s Equations (Huray, 2010)
- The ideational contents of Aristotle?s book entitled ?Metaphysics? as rendered in the Greek texts translated in ? Oxford edition?
- The underlying prototype of any ?no-smoking? sign (E36)
- The common ideas of the plots of the movie "The Seven Samurai" by Akira Kurosawa and the movie ?The Magnificent Seven? by John Sturges
- The image content of the photo of the Allied Leaders at Yalta published by UPI, 1945 (E36)
- The character "Little Red Riding Hood" variants of which appear amongst others in Grimm brothers? ?Rotk?ppchen?, other oral fairy tales and the film 'Hoodwinked'
- The place "Havnor" as invented by Ursula K. Le Guin for her ?Earthsea? book series, the related maps and appearing in derivative works based on these novels


In First Order Logic:
E89(x) ? E28(x)
    """

    P129_is_about: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P148_has_component: Tuple[object, ...] = ()  # Range: E89PropositionalObject
    P148_is_component_of: Tuple[object, ...] = ()  # Range: E89PropositionalObject
    P67_refers_to: Tuple[object, ...] = ()  # Range: E1CRMEntity
    _typename: str = 'E89PropositionalObject'
