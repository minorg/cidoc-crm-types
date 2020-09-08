from .e89_propositional_object import E89PropositionalObject
from .e90_symbolic_object import E90SymbolicObject
from dataclasses import dataclass


@dataclass
class E73InformationObject(E90SymbolicObject, E89PropositionalObject):

