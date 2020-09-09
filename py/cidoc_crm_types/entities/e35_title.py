from .e33_linguistic_object import E33LinguisticObject
from .e41_appellation import E41Appellation
from dataclasses import dataclass


@dataclass
class E35Title(E33LinguisticObject, E41Appellation):
    """
Scope note:
This class comprises textual strings that within a cultural context can be clearly identified as titles due to their form. Being a subclass of E41 Appellation, E35 Title can only be used when such a string is actually used as a title of a work, such as a text, an artwork, or a piece of music.

Titles are proper noun phrases or verbal phrases, and should not be confused with generic object names such as &#8220;chair&#8221;, &#8220;painting&#8221; or &#8220;book&#8221; (the latter are common nouns that stand for instances of E55 Type). Titles may be assigned by the creator of the work itself, or by a social group.

This class also comprises the translations of titles that are used as surrogates for the original titles in different social contexts.


Examples:
- &#8220;The Merchant of Venice&#8221; (McCullough, 2005)
- &#8220;Mona Lisa&#8221; (Mohen, 2006)
- &#8220;La Pie or The Magpie&#8221; (Bortolatto, 1981)
- &#8220;Lucy in the Sky with Diamonds&#8221; (Lennon, 1967)


In First Order Logic:
E35(x) &#8835; E33(x)
E35(x) &#8835; E41(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E35_Title"
