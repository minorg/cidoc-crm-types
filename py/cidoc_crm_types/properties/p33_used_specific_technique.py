from .p16_used_specific_object import P16UsedSpecificObject
from dataclasses import dataclass


@dataclass
class P33UsedSpecificTechnique(P16UsedSpecificObject):
    """
Scope note:
This property identifies a specific instance of E29 Design or Procedure in order to carry out an instance of E7 Activity or parts of it.

The property differs from P32 used general technique (was technique of) in that P33 refers to an instance of E29 Design or Procedure, which is a concrete information object in its own right rather than simply being a term or a method known by tradition.

Typical examples would include intervention plans for conservation or the construction plans of a building


Examples:
- Ornamentation of silver cup 232 (E11) used specific technique 'Instructions for golden chase work by A N Other' (E29)
- Rebuilding of Reichstag (E11) used specific technique Architectural plans by Foster and Partners (E29)


In First Order Logic:
P33(x,y) &#8835; E7(x)
P33(x,y) &#8835; E29(y)
P33(x,y) &#8835; P16(x,y)
    """

    URI = "http://erlangen-crm.org/current/P33_used_specific_technique"
