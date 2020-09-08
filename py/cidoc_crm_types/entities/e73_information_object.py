from .e89_propositional_object import E89PropositionalObject
from .e90_symbolic_object import E90SymbolicObject
from dataclasses import dataclass


@dataclass
class E73InformationObject(E89PropositionalObject, E90SymbolicObject):
    """
Scope note:
This class comprises identifiable immaterial items, such as a poems, jokes, data sets, images, texts, multimedia objects, procedural prescriptions, computer program code, algorithm or mathematical formulae, that have an objectively recognizable structure and are documented as single units. The encoding structure known as a "named graph" also falls under this class, so that each "named graph" is an instance of E73 Information Object.
An instance of E73 Information Object does not depend on a specific physical carrier, which can include human memory, and it can exist on one or more carriers simultaneously.

Instances of E73 Information Object of a linguistic nature should be declared as instances of the E33 Linguistic Object subclass. Instances of E73 Information Object of a documentary nature should be Definition of the CIDOC Conceptual Reference Model version 6.2.8 34 declared as instances of the E31 Document subclass. Conceptual items such as types and classes are not instances of E73 Information Object, nor are ideas without a reproducible expression.


Examples:
- image BM000038850.JPG from the Clayton Herbarium in London (E31)
- E. A. Poe's "The Raven" (Poe, 1869)
- the movie "The Seven Samurai" by Akira Kurosawa (Mellen, 2002)
- the Maxwell Equations (Huray, 2010)
- The Getty AAT as published as Linked Open Data, accessed 1/10/2014


In First Order Logic: 
E73(x) ? E89(x)  
E73(x) ? E90(x)
    """

    _typename: str = 'E73InformationObject'
