from dataclasses import dataclass
from .e89_propositional_object import E89PropositionalObject
from .e90_symbolic_object import E90SymbolicObject

@dataclass
class E73InformationObject(E89PropositionalObject, E90SymbolicObject):
    pass
