from .p130_shows_features_of import P130ShowsFeaturesOf
from dataclasses import dataclass


@dataclass
class P128Carries(P130ShowsFeaturesOf):
    """
Scope note:
This property identifies an instance E90 Symbolic Object carried by an instance of E18 Physical Thing.
Since an instance of E90 Symbolic Object is defined as an immaterial idealization over potentially multiple carriers, any individual realization on a particular physical carrier may be defective, due to deterioration or shortcomings in the process of creating the realization compared to the intended ideal. As long as such defects do not substantially affect the complete recognition of the respective symbolic object, it is still regarded as carrying an instance of this E90 Symbolic Object. If these defects are of scholarly interest, the particular realization can be modelled as an instance of E25 Human-Made Feature. Note, that any instance of E90 Symbolic Object incorporated (P165) in the carried symbolic object is also carried by the same instance of E18 Physical Thing.


Examples:
- Matthew's paperback copy of Reach for the Sky (E18) carries the text of Reach for the Sky (E73)


In First Order Logic:
P128(x,y) &#8835; E18(x)
P128(x,y) &#8835; E90(y)
P128(x,y) &#8835; P130(x,y)
    """

    URI = "http://erlangen-crm.org/current/P128_carries"
