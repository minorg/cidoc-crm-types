from dataclasses import dataclass


@dataclass
class P148HasComponent:
    """
Scope note:
This property associates an instance of E89 Propositional Object with a structural part of it that is by itself an instance of E89 Propositional Object.
This property is transitive


Examples:
- Dante's "Divine Comedy" (E89) has component Dante's "Hell" (E89)


In First Order Logic:
P148(x,y) &#8835; E89(x)
P148(x,y) &#8835; E89(y)
    """

    URI = "http://erlangen-crm.org/current/P148_has_component"
