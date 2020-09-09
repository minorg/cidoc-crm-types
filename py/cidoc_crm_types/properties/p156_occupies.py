from .p157i_provides_reference_space_for import P157iProvidesReferenceSpaceFor
from .p53_has_former_or_current_location import P53HasFormerOrCurrentLocation
from dataclasses import dataclass


@dataclass
class P156Occupies(P53HasFormerOrCurrentLocation, P157iProvidesReferenceSpaceFor):
    """
Scope note:
This property describes the largest volume in space, an instance of E53 Place, that an instance of E18 Physical Thing has occupied at any time during its existence, with respect to the reference space relative to the physical thing itself. This allows for describing the thing itself as a place that may contain other things, such as a box that may contain coins. In other words, it is the volume that contains all the points which the thing has covered at some time during its existence. The reference space for the associated place must be the one that is permanently at rest (P157 is at rest relative to) relative to the physical thing. For instances of E19 Physical Objects it is the one which is at rest relative to the object itself, i.e. which moves together with the object. For instances of E26 Physical Feature it is one which is at rest relative to the physical feature itself and the surrounding matter immediately connected to it. Therefore there is a 1:1 relation between the instance E18 Physical Thing and the instance of E53 Place it occupies. We include in the occupied space the space filled by the matter of the physical thing and all its inner spaces.

This property implies the fully developed path from E18 Physical Thing through P196 defines, E92 Spacetime Volume, P161 has spatial projection, E53 Place. However, in contrast to P156 occupies, the property P161 has spatial projection does not constrain the reference space of the referred instance of E53 Place.

In contrast to P156 occupies, for the property P53 has former or current location the following holds:
- It does not constrain the reference space of the referred instance of E53 Place.
- It identifies a possibly wider instance of E53 Place at which a thing is or has been for some unspecified time span.
- If the reference space of the referred instance of E53 Place is not at rest with respect to the physical thing found there, the physical thing may move away after some time to another place and/or may have been at some other place before. The same holds for the fully developed path from E18 Physical Thing through P196 defines, E92 Spacetime Volume, P161 has spatial projection, E53 Place. 


In First Order Logic:
P156(x,y) &#8835; E53(y)
P156(x,y) &#8835; E18(x)
P156 (x,y) = [E18(x) &#8743; E53(y) &#8743; P196(x,z) &#8743; P161(z,y) &#8743; P157(y,x)]
    """

    URI = "http://erlangen-crm.org/current/P156_occupies"
