from dataclasses import dataclass


@dataclass
class P74HasCurrentOrFormerResidence:
    """
Scope note:
This property describes the current or former place of residence (an instance of E53 Place) of an instance of E39 Actor.

The residence may be either the place where the actor resides, or a legally registered address of any kind.


Examples:
- Queen Elizabeth II (E39) has current or former residence Buckingham Palace (E53)


In First Order Logic:
P74(x,y) &#8835; E39(x)
P74(x,y) &#8835; E53(y)
    """

    URI = "http://erlangen-crm.org/current/P74_has_current_or_former_residence"
