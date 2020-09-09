from .e7_activity import E7Activity
from dataclasses import dataclass


@dataclass
class E87CurationActivity(E7Activity):
    """
Scope note:
This class comprises the activities that result in the continuity of management and the preservation and evolution of instances of E78 Collection, following an implicit or explicit curation plan.

It specializes the notion of activity into the curation of a collection and allows the history of curation to be recorded.

Items are accumulated and organized following criteria like subject, chronological period, material type, style of art etc. and can be added or removed from an instance of E78 Collection for a specific purpose and/or audience. The initial aggregation of items of a collection is regarded as an instance of E12 Production Event while the activity of evolving, preserving and promoting a collection is regarded as an instance of E87 Curation Activity.


Examples:
- the curation of Mikael Heggelund Foslie's coralline red algae Herbarium 1876 &#8211; 1909 (when Foslie died), now at Museum of Natural History and Archaeology, Norway


In First Order Logic:
E87(x) &#8835; E7(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E87_Curation_Activity"
