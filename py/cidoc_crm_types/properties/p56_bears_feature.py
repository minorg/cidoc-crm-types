from .p46_is_composed_of import P46IsComposedOf
from dataclasses import dataclass


@dataclass
class P56BearsFeature(P46IsComposedOf):
    """
Scope note:
This property links an instance of E19 Physical Object to an instance of E26 Physical Feature that it bears.
An instance of E26 Physical Feature can only exist on one object. One object may bear more than one E26 Physical Feature. An instance of E27 Site should be considered as an instance of E26 Physical Feature on the surface of the Earth.
An instance B of E26 Physical Feature being a detail of the structure of another instance A of E26 Physical Feature can be linked to B by use of the property P46 is composed of (forms part of). This implies that the subfeature B is P56i found on the same E19 Physical Object as A. 
P56 bears feature (is found on) is a shortcut. A more detailed representation can make use of the fully developed (i.e. indirect) path &#8216;E19 Physical Object&#8217;,through, &#8216;P59 has section&#8217;, &#8216;E53 Place&#8217;, &#8216;P53i is former or current location of&#8217;, to, &#8216;E26 Physical Feature&#8217;.


Examples:
- silver cup 232 (E22) bears feature 32 mm scratch on silver cup 232 (E26)


In First Order Logic:
P56(x,y) &#8835;E19(x)
P56(x,y) &#8835; E26(y)
P56(x,y) &#8835; P46(x,y)
    """

    URI = "http://erlangen-crm.org/current/P56_bears_feature"
