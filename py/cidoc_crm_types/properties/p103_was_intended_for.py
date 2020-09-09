from dataclasses import dataclass


@dataclass
class P103WasIntendedFor:
    """
Scope note:
This property links an instance of E71 Human-Made Thing to an instance of E55 Type describing its intended usage.

It creates a relation between specific human-made things, both physical and immaterial, to types of intended methods and techniques of use. Note: A link between specific human-made things and a specific use activity should be expressed using P19 was intended use of (was made for).


Examples:
- this plate (E22) was intended for being destroyed at wedding reception (E55)


In First Order Logic:
P103(x,y) &#8835; E71(x)
P103(x,y) &#8835; E55(y)
    """

    URI = "http://erlangen-crm.org/current/P103_was_intended_for"
