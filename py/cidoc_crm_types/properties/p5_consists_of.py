from dataclasses import dataclass


@dataclass
class P5ConsistsOf:
    """
Scope note:
This property describes the decomposition of an instance of E3 Condition State into discrete, subsidiary states.

It is assumed that the sub-states into which the condition state is analysed form a logical whole - although the entire story may not be completely known &#8211; and that the sub-states are in fact constitutive of the general condition state. For example, a general condition state of &#8220;in ruins&#8221; may be decomposed into the individual stages of decay.
This property is transitive.


Examples:
- The Condition State of the ruined Parthenon (E3) consists of the bombarded state after the explosion of a Venetian shell in 1687 (E3)


In First Order Logic:
P5(x,y) &#8835; E3(x)
P5(x,y) &#8835; E3(y)
    """

    URI = "http://erlangen-crm.org/current/P5_consists_of"
