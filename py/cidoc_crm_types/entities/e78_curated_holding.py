from .e24_physical_human_made_thing import E24PhysicalHumanMadeThing
from dataclasses import dataclass


@dataclass
class E78CuratedHolding(E24PhysicalHumanMadeThing):
    """
Scope note:
This class comprises aggregations of instances of E18 Physical Thing that are assembled and maintained (&#8220;curated&#8221; and &#8220;preserved,&#8221; in museological terminology) by one or more instances of E39 Actor over time for a specific purpose and audience, and according to a particular collection development plan. Typical instances of curated holdings are museum collections, archives, library holdings and digital libraries. A digital library is regarded as an instance of E18 Physical Thing because it requires keeping physical carriers of the electronic content.

Items may be added or removed from an E78 Curated Holding in pursuit of this plan. This class should not be confused with the E39 Actor maintaining the E78 Curated Holding often referred to with the name of the E78 Curated Holding (e.g. &#8220;The Wallace Collection decided&#8230;&#8221;). 

Collective objects in the general sense, like a tomb full of gifts, a folder with stamps or a set of chessmen, Definition of the CIDOC Conceptual Reference Model version 6.2.8 36
should be documented as instances of E19 Physical Object, and not as instances of E78 Curated Holding. This is because they form wholes either because they are physically bound together or because they are kept together for their functionality.


Examples:
the John Clayton Herbarium
&#61607; the Wallace Collection (Ingamells, 1990)
&#61607; Mikael Heggelund Foslie&#8217;s coralline red algae Herbarium at Museum of Natural History and Archaeology, Trondheim, Norway
&#61607; The Digital Collections of the Munich DigitiZation Center (MDZ) accessible via https://www.digitale-sammlungen.de/ at least in January 2018


In First Order Logic:
E78(x) &#8835; E24(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E78_Curated_Holding"
