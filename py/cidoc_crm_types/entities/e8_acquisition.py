from .e7_activity import E7Activity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E8Acquisition(E7Activity):
    """
Scope note:
This class comprises transfers of legal ownership from one or more instances of E39 Actor to one or more other instances of E39 Actor.

The class also applies to the establishment or loss of ownership of instances of E18 Physical Thing. It does not, however, imply changes of any other kinds of right. The recording of the donor and/or recipient is optional. It is possible that in an instance of E8 Acquisition there is either no donor or no recipient. Depending on the circumstances, it may describe:
1. the beginning of ownership
2. the end of ownership
3. the transfer of ownership
4. the acquisition from an unknown source
5. the loss of title due to destruction of the item

It may also describe events where a collector appropriates legal title, for example by annexation or field collection. The interpretation of the museum notion of "accession" differs between institutions. The CIDOC CRM therefore models legal ownership (E8 Acquisition) and physical custody (E10 Transfer of Custody) separately. Institutions will then model their specific notions of accession and deaccession as combinations of these.


Examples:
- the collection of a hammer-head shark of the genus Sphyrna (Carchariniformes) XXXtbc by John Steinbeck and Edward Ricketts at Puerto Escondido in the Gulf of Mexico on March 25th, 1940. (Steinbeck, 2000)
- the acquisition of El Greco?s painting entitled ?The Apostles Peter and Paul? by the State Hermitage in Saint Petersburg
- the loss of my stuffed chaffinch ?Fringilla coelebs Linnaeus, 1758? due to insect damage last year


In First Order Logic:
E8(x) ? E7(x)
    """

    P24_transferred_title_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
