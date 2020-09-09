from dataclasses import dataclass


@dataclass
class P126Employed:
    """
Scope note:
This property identifies the instance of E57 Material employed in an instance of E11 Modification.

The instance of E57 Material used during the instance of E11 Modification does not necessarily become incorporated into the instance of E24 Physical Human-Made Thing that forms the subject of the instance of E11 Modification.


Examples:
- the repairing of the Queen Mary (E11) employed Steel (E57)
- distilled water (E57) was employed in the restoration of the Sistine Chapel (E11)


In First Order Logic:
P126(x,y) &#8835; E11(x)
P126(x,y) &#8835; E57(y)
    """

    URI = "http://erlangen-crm.org/current/P126_employed"
