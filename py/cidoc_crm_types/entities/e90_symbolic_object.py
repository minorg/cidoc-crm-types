from dataclasses import dataclass
from .e72_legal_object import E72LegalObject
from .e28_conceptual_object import E28ConceptualObject

@dataclass
class E90SymbolicObject(E72LegalObject, E28ConceptualObject):
    pass
