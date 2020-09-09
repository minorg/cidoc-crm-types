from dataclasses import dataclass


@dataclass
class P104IsSubjectTo:
    """
Scope note:
This property links a particular instance of E72 Legal Object to the instances of E30 Right to which it is subject.

The Right is held by an E39 Actor as described by P75 possesses (is possessed by).


Examples:
- Beatles back catalogue (E72) is subject to reproduction right on Beatles back catalogue (E30)


In First Order Logic:
P104(x,y) &#8835; E72(x)
P104(x,y) &#8835; E30(y)
    """

    URI = "http://erlangen-crm.org/current/P104_is_subject_to"
