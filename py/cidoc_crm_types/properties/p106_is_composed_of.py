from dataclasses import dataclass


@dataclass
class P106IsComposedOf:
    """
Scope note:
This property associates an instance of E90 Symbolic Object with a part of it that is by itself an instance of E90 Symbolic Object, such as fragments of texts or clippings from an image.
This property is transitive.


Examples:
- This Scope note P106 (E33) is composed of fragments of texts (E33)
- 'recognizable' P106 (E90) is composed of 'ecognizabl' (E90)


In First Order Logic:
P106(x,y) &#8835; E90(x)
P106(x,y) &#8835; E90(y)
    """

    URI = "http://erlangen-crm.org/current/P106_is_composed_of"
