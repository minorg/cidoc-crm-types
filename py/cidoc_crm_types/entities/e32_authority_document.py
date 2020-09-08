from .e31_document import E31Document
from dataclasses import dataclass


@dataclass
class E32AuthorityDocument(E31Document):
    """
Scope note:
This class comprises encyclopaedia, thesauri, authority lists and other documents that define terminology or conceptual systems for consistent use.


Examples:
- Webster's Dictionary
- Getty Art and Architecture Thesaurus (Getty Trust, 1990)
- the CIDOC Conceptual Reference Model (Gergatsoulis, M. et al., 2010) 


In First Order Logic:
E32(x) ? E31(x)
    """

    _typename: str = 'E32AuthorityDocument'
