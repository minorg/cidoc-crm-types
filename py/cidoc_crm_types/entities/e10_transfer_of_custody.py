from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E10TransferofCustody(E7Activity):
    """
Scope note:
This class comprises transfers of physical custody of objects between instances of E39 Actor. 

The recording of the donor and/or recipient is optional. It is possible that in an instance of E10 Transfer of Custody there is either no donor or no recipient. Depending on the circumstances it may describe:
1. the beginning of custody
2. the end of custody
3. the transfer of custody
4. the receipt of custody from an unknown source
5. the declared loss of an object

The distinction between the legal responsibility for custody and the actual physical possession of the object should be expressed using the property P2 has type (is type of). A specific case of transfer of custody is theft. The sense of physical possession requires that the object of custody is in the hands of the keeper at least with a part representative for the whole. The way, in which a representative part is defined, should ensure that it is unambiguous who keeps a part and who the whole and should be consistent with the identity criteria of the kept instance of E18 Physical Thing. For instance, in the case of a set of cutlery we may require the majority of pieces having been in the hands of the actor regardless which individual pieces are kept over time.

The interpretation of the museum notion of "accession" differs between institutions. The CIDOC CRM therefore models legal ownership and physical custody separately. Institutions will then model their specific notions of accession and deaccession as combinations of these.


Examples:
- the delivery of the paintings by Secure Deliveries Inc. to the National Gallery
- the return of Picasso?s ?Guernica? to Madrid?s Prado in 1981 (Chipp, 1988)


In First Order Logic:
E10(x) ? E7(x)
    """

    P30_transferred_custody_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
