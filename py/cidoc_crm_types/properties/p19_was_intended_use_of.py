from dataclasses import dataclass


@dataclass
class P19WasIntendedUseOf:
    """
Scope note:
This property relates an instance of E7 Activity with instances of E71 Human-Made Thing, created specifically for use in the activity.

This is distinct from the intended use of an item in some general type of activity such as the book of common prayer which was intended for use in Church of England services (see P101 had as general use (was use of)).


Examples:
- Lady Diana Spencer's wedding dress (E71) was made for Wedding of Prince Charles and Lady Diana Spencer (E7) mode of use To Be Worn (E55)


In First Order Logic:
P19(x,y) &#8835; E7(x)
P19(x,y) &#8835; E71(y)
P19(x,y,z) &#8835; [P19(x,y) &#8743; E55(z)]
    """

    URI = "http://erlangen-crm.org/current/P19_was_intended_use_of"
