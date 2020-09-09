from .p130i_features_are_also_found_on import P130iFeaturesAreAlsoFoundOn
from dataclasses import dataclass


@dataclass
class P73HasTranslation(P130iFeaturesAreAlsoFoundOn):
    """
Scope note:
This property links an instance of E33 Linguistic Object (A), to another instance of E33 Linguistic Object (B) which is the translation of A.

When an instance of E33 Linguistic Object is translated into a new language a new instance of E33 Linguistic Object is created, despite the translation being conceptually similar to the source.
This property is transitive.


Examples:
- "Les Baigneurs" (E33) has translation "The Bathers" (E33)


In First Order Logic:
P73(x,y) &#8835; E33(x)
P73(x,y) &#8835; E33(y)
P73(x,y) &#8835; P130(y,x)
    """

    URI = "http://erlangen-crm.org/current/P73_has_translation"
