from .p141_assigned import P141Assigned
from dataclasses import dataclass


@dataclass
class P40ObservedDimension(P141Assigned):
    """
Scope note:
This property records the dimension that was observed in an E16 Measurement Event.
E54 Dimension can be any quantifiable aspect of E70 Thing. Weight, image colour depth and monetary value are dimensions in this sense. One measurement activity may determine more than one dimension of one object.
Dimensions may be determined either by direct observation or using recorded evidence. In the latter case the measured Thing does not need to be present or extant.
Even though knowledge of the value of a dimension requires measurement, the dimension may be an object of discourse prior to, or even without, any measurement being made.


Examples:
- 31 August 1997 measurement of height of silver cup 232 (E16) observed dimension silver cup 232 height (E54) has unit mm (E58), has value 224 (E60)


In First Order Logic:
P40(x,y) &#8835; E16(x)
P40(x,y)&#8835; E54(y)
P40(x,y) &#8835; P141(x,y)
    """

    URI = "http://erlangen-crm.org/current/P40_observed_dimension"
