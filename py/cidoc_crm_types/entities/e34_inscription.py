from .e33_linguistic_object import E33LinguisticObject
from .e37_mark import E37Mark
from dataclasses import dataclass


@dataclass
class E34Inscription(E33LinguisticObject, E37Mark):
    """
Scope note:
This class comprises recognisable, texts attached to instances of E24 Physical Human-Made Thing.

The transcription of the text can be documented in a note by P3 has note: E62 String. The alphabet used can be documented by P2 has type: E55 Type. This class does not intend to describe the idiosyncratic characteristics of an individual physical embodiment of an inscription, but the underlying prototype. The physical embodiment is modelled in the CIDOC CRM as instances of E24 Physical Human-Made Thing.

The relationship of a physical copy of a book to the text it contains is modelled using E18 Physical Thing. P128 carries (is carried by): E33 Linguistic Object.


Examples:
- "keep off the grass" on a sign stuck in the lawn of the quad of Balliol College
- The text published in Corpus Inscriptionum Latinarum V 895
- Kilroy was here


In First Order Logic:
E34(x) ? E33(x)
E34(x) ? E37(x)
    """

    __typename: str = 'E34Inscription'
