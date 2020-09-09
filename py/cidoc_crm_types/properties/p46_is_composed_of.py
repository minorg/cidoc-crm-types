from dataclasses import dataclass


@dataclass
class P46IsComposedOf:
    """
Scope note:
This property associates an instance of E18 Physical Thing with another instance of Physical Thing that forms part of it. The spatial extent of the composing part is included in the spatial extent of the whole.

Component elements, since they are themselves instances of E18 Physical Thing, may be further analysed into sub-components, thereby creating a hierarchy of part decomposition. An instance of E18 Physical Thing may be shared between multiple wholes, for example two buildings may share a common wall. This property does not specify when and for how long a component element resided in the respective whole. If a component is not part of a whole from the beginning of existence or until the end of existence of the whole, the classes E79 Part Addition and E90 Part Removal can be used to document when a component became part of a particular whole and/or when it stopped being a part of it. For the time-span of being part of the respective whole, the component is completely contained in the place the whole occupies.

This property is intended to describe specific components that are individually documented, rather than general aspects. Overall descriptions of the structure of an instance of E18 Physical Thing are captured by the P3 has note property.

The instances of E57 Material of which an item of E18 Physical Thing is composed should be documented using P45 consists of (is incorporated in).


Examples:
- the Royal carriage (E22) forms part of the Royal train (E22)
- the "Hog's Back" (E24) forms part of the "Fosseway" (E24)


In First Order Logic:
P46(x,y) &#8835; E18(x)
P46(x,y) &#8835; E18(y)
P46(x,y) &#8835; P132(x,y)
P46(x,y) &#8835; (&#61476;uzw)[E93(u) &#8743; P166 (x,u) &#8743; E52(z) &#8743; P164(u,z) &#8743; E93(w) &#8743; P166 (y,w) &#8743;
P164(w,z) &#8743; P10(w,u)]
    """

    URI = "http://erlangen-crm.org/current/P46_is_composed_of"
