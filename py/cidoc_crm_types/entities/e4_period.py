from .e2_temporal_entity import E2TemporalEntity
from .e92_spacetime_volume import E92SpacetimeVolume
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E4Period(E2TemporalEntity, E92SpacetimeVolume):
    """
Scope note:
This class comprises sets of coherent phenomena or cultural manifestations occurring in time and space.

It is the social or physical coherence of these phenomena that identify an instance of E4 Period and not the associated spatiotemporal extent. This extent is only the ?ground? or space in an abstract physical sense that the actual process of growth, spread and retreat has covered. Consequently, different periods can overlap and coexist in time and space, such as when a nomadic culture exists in the same area and time as a sedentary culture. This also means that overlapping land use rights, common among first nations, amounts to overlapping periods.

Often, this class is used to describe prehistoric or historic periods such as the ?Neolithic Period?, the ?Ming Dynasty? or the ?McCarthy Era?, but also geopolitical units and activities of settlements are regarded as special cases of E4 Period. However, there are no assumptions about the scale of the associated phenomena. In particular all events are seen as synthetic processes consisting of coherent phenomena. Therefore E4 Period is a superclass of E5 Event. For example, a modern clinical birth, an instance of E67 Birth, can be seen as both a single event, i.e., an instance of E5 Event, and as an extended period, i.e., an instance of E4 Period, that consists of multiple physical processes and complementary activities performed by multiple instances of E39 Actor.

As the actual extent of an instance of E4 Period in spacetime we regard the trajectories of the participating physical things during their participation in an instance of E4 Period. This includes the open spaces via which these things have interacted and the spaces by which they had the potential to interact during that period or event in the way defined by the type of the respective period or event. Examples include the air in a meeting room transferring the voices of the participants. Since these phenomena are fuzzy, we assume the spatiotemporal extent to be contiguous, except for cases of phenomena spreading out over islands or other separated areas, including geopolitical units distributed over disconnected areas such as islands or colonies.

Whether the trajectories necessary for participants to travel between these areas are regarded as part of the spatiotemporal extent or not has to be decided in each case based on a concrete analysis, taking use of the sea for other purposes than travel, such as fishing, into consideration. One may also argue that the activities to govern disconnected areas imply travelling through spaces connecting them and that these areas hence are spatially connected in a way, but it appears counterintuitive to consider for instance travel routes in international waters as extensions of geopolitical units.


We model E4 Period as a subclass of E2 Temporal Entity and of E92 Spacetime Volume. The latter is intended as a phenomenal spacetime volume as defined in CIDOC CRMgeo (Doerr and Hiebel, 2013). By virtue of this multiple inheritance we can discuss the physical extent of an instance of E4 Period without representing each instance of it together with an instance of its associated spacetime volume. This model combines two quite different kinds of substance: an instance of E4 Period is a phenomena while an instance of E92 Spacetime Volume is an aggregation of points in spacetime. However, the real spatiotemporal extent of an instance of E4 Period is regarded to be unique to it due to all its details and fuzziness; its identity and existence depends uniquely on the identity of the instance of E4 Period. Therefore this multiple inheritance is unambiguous and effective and furthermore corresponds to the intuitions of natural language.

Typical use of this class in cultural heritage documentation is for documenting cultural and artistic periods. There are two different conceptualisations of ?artistic style?, defined either by physical features or by historical context. For example, ?Impressionism? can be viewed as a period in the European sphere of influence lasting from approximately 1870 to 1905 during which paintings with particular characteristics were produced by a group of artists that included (among others) Monet, Renoir, Pissarro, Sisley and Degas. Alternatively, it can be regarded as a style applicable to all paintings sharing the characteristics of the works produced by the Impressionist painters, regardless of historical context. The first interpretation is an instance of E4 Period, and the second defines morphological object types that fall under E55 Type.

A geopolitical unit as a specific case of an instance of E4 Period is the set of activities and phenomena related to the claim of power, the consequences of belonging to a jurisdictional area and an administrative system that establishes a geopolitical unit. Examples from the modern period are countries or administrative areas of countries such as districts whose actions and structures define activities and phenomena in the area that they intend to govern. The borders of geopolitical units are often defined in contracts or treaties although they may deviate from the actual practice. The spatiotemporal properties of Geopolitical units can be modelled through the properties inherited from E92 Spacetime Volume. 

Another specific case of an instance of E4 Period is the actual extent of the set of activities and phenomena as evidenced by their physical traces that define a settlement, such as the populated period of Nineveh.


Examples:
- Jurassic (Hallam, 1975)
- Populated Period of Nineveh
- Imperial Rome under Marcus Aurelius
- European Bronze Age (Harrison, c2004)
- Italian Renaissance (Macdonald, 1992)
- Thirty Years War (Lee, 1991)
- Sturm und Drang (Berkoff, 2013)
- Cubism (Cox, 2000)


In First Order Logic: 
E4(x) ? E2(x)
E4(x) ? E92(x)
    """

    P7_took_place_at: Tuple[object, ...] = ()  # Range: E53Place
    P8_took_place_on_or_within: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    __typename: str = 'E4Period'
