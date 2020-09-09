from .p11_had_participant import P11HadParticipant
from dataclasses import dataclass


@dataclass
class P14CarriedOutBy(P11HadParticipant):
    """
Scope note:
This property describes the active participation of an instance of E39 Actor in an instance of E7 Activity.

It implies causal or legal responsibility. The P14.1 in the role of property of the property specifies the nature of an Actor&#8217;s participation.


Examples:
- the painting of the Sistine Chapel (E7) carried out by Michaelangelo Buonaroti (E21) in the role of master craftsman (E55)


In First Order Logic:
P14 (x,y) &#8835; E7(x)
P14 (x,y)&#8835; E39(y)
P14 (x,y) &#8835; P11(x,y)
P14(x,y,z) &#8835; [P14(x,y) &#8743; E55(z)]
    """

    URI = "http://erlangen-crm.org/current/P14_carried_out_by"
