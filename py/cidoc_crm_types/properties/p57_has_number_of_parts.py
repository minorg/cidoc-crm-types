from dataclasses import dataclass


@dataclass
class P57HasNumberOfParts:
    """
Scope note:
This property documents the E60 Number of parts of which an instance of E19 Physical Object is composed.

This may be used as a method of checking inventory counts with regard to aggregate or collective objects. What constitutes a part or component depends on the context and requirements of the documentation. Normally, the parts documented in this way would not be considered as worthy of individual attention.

For a more complete description, objects may be decomposed into their components and constituents using P46 is composed of (forms parts of) and P45 consists of (is incorporated in). This allows each element to be described individually.

Examples:
- chess set 233 (E22) has number of parts 33 (E60)

In First Order Logic:
P57(x,y) &#8835; E19(x)
P57(x,y) &#8835; E60(y)
    """

    URI = "http://erlangen-crm.org/current/P57_has_number_of_parts"
