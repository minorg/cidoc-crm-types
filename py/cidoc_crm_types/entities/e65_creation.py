from .e63_beginning_of_existence import E63BeginningofExistence
from .e7_activity import E7Activity
from dataclasses import dataclass


@dataclass
class E65Creation(E7Activity, E63BeginningofExistence):
    """
Scope note:
This class comprises events that result in the creation of conceptual items or immaterial products, such as legends, poems, texts, music, images, movies, laws, types etc.


Examples:
- the framing of the U.S. Constitution (Farrand, 1913)
- the drafting of U.N. resolution 1441 (United Nations Security Council, 2002)


In First Order Logic:
E65(x) &#8835; E7(x)
E65(x) &#8835; E63(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E65_Creation"
