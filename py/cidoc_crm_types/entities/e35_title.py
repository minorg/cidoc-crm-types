from .e33_linguistic_object import E33LinguisticObject
from .e41_appellation import E41Appellation
from dataclasses import dataclass


@dataclass
class E35Title(E41Appellation, E33LinguisticObject):
    """
Scope note:
This class comprises textual strings that within a cultural context can be clearly identified as titles due to their form. Being a subclass of E41 Appellation, E35 Title can only be used when such a string is actually used as a title of a work, such as a text, an artwork, or a piece of music.

Titles are proper noun phrases or verbal phrases, and should not be confused with generic object names such as ?chair?, ?painting? or ?book? (the latter are common nouns that stand for instances of E55 Type). Titles may be assigned by the creator of the work itself, or by a social group.

This class also comprises the translations of titles that are used as surrogates for the original titles in different social contexts.


Examples:
- ?The Merchant of Venice? (McCullough, 2005)
- ?Mona Lisa? (Mohen, 2006)
- ?La Pie or The Magpie? (Bortolatto, 1981)
- ?Lucy in the Sky with Diamonds? (Lennon, 1967)


In First Order Logic:
E35(x) ? E33(x)
E35(x) ? E41(x)
    """

    __typename: str = 'E35Title'
