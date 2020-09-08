from .e4_period import E4Period
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E5Event(E4Period):
    """
Scope note:
This class comprises distinct, delimited and coherent processes and interactions of a material nature, in cultural, social or physical systems, involving and affecting instances of E77 Persistent Item in a way characteristic of the kind of process. Typical examples are meetings, births, deaths, actions of decision taking, making or inventing things, but also more complex and extended ones such as conferences, elections, building of a castle, or battles.

While the continuous growth of a tree lacks the limits characteristic of an event, its germination from a seed does qualify as an event. Similarly the blowing of the wind lacks the distinctness and limits of an event, but a hurricane, flood or earthquake would qualify as an event. Mental processes are considered as events, in cases where they are connected with the material externalization of their results; for example the creation of a poem, a performance or a change of intention that becomes obvious from subsequent actions or declarations. 

The effects of an instance of E5 Event may not lead to relevant permanent changes of properties or relations of the items involved in it, for example an unrecorded performances. Of course, in order to be documented, some kind of evidence for an event must exist, be it witnesses, traces or products of the event. While instances of E4 Period always require some form of coherence between its constituent phenomena, in addition, the essential constituents of instances of E5 Event should contribute to an overall effect; for example the statements made during a meeting and the listening of the audience.

Viewed at a coarse level of detail, an instance of E5 Event may appear as if it had an ?instantaneous? overall effect, but any process or interaction of material nature in reality have an extent in time and space. At a fine level, instances of E5 Event may be analyzed into component phenomena and phases within a space and timeframe, and as such can be seen as a period, regardless of the size of the phenomena. The reverse is not necessarily the case: not all instances of E4 Period give rise to a noteworthy overall effect and are thus not instances of E5 Event.


Examples:
- the birth of Cleopatra (E67) (Pomeroy, 1984)
- the destruction of Herculaneum by volcanic eruption in 79 AD (E6) (Camardo, 2013)
- World War II (E7) (Barber, 1994)
- the Battle of Stalingrad (E7) (Hoyt, 1993)
- the Yalta Conference (E7) (Harbutt, 2010)
- my birthday celebration 28-6-1995 (E7)
- the falling of a tile from my roof last Sunday
- the CIDOC Conference 2003 (E7)


In First Order Logic:
E5(x) ? E4(x)
    """

    P11_had_participant: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P12_occurred_in_the_presence_of: Tuple[object, ...] = ()  # Range: E77PersistentItem
    P20_was_purpose_of: Tuple[object, ...] = ()  # Range: E7Activity
