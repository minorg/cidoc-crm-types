from dataclasses import dataclass


@dataclass
class P45ConsistsOf:
    """
Scope note:
This property identifies the instances of E57 Materials of which an instance of E18 Physical Thing is composed.

All physical things consist of physical materials. P45 consists of (is incorporated in) allows the different Materials to be recorded. P45 consists of (is incorporated in) refers here to observed Material as opposed to the consumed raw material.

A Material, such as a theoretical alloy, may not have any physical instances.


Examples:
- silver cup 232 (E22) consists of silver (E57)


In First Order Logic:
P45(x,y) &#8835; E18(x)
P45(x,y) &#8835; E57(y)
    """

    URI = "http://erlangen-crm.org/current/P45_consists_of"
