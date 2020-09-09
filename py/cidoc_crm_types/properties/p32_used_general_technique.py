from .p125_used_object_of_type import P125UsedObjectOfType
from dataclasses import dataclass


@dataclass
class P32UsedGeneralTechnique(P125UsedObjectOfType):
    """
Scope note:
This property identifies the technique or method, modelled as an instance of E55 Type, that was employed in an instance of E7 Activity.

These techniques should be drawn from an external E55 Type hierarchy of consistent terminology of general techniques or methods such as embroidery, oil-painting, carbon dating, etc. Specific documented techniques should be described as instances of E29 Design or Procedure. This property identifies the technique that was employed in an act of modification. 


Examples:
- ornamentation of silver cup 113 (E11) used general technique gold-plating (E55) (Design or Procedure Type)


In First Order Logic:
P32(x,y) &#8835; E7(x)
P32(x,y) &#8835; E55(y)
P32(x,y) &#8835; P125(x,y)
    """

    URI = "http://erlangen-crm.org/current/P32_used_general_technique"
