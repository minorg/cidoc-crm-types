from .p12_occurred_in_the_presence_of import P12OccurredInThePresenceOf
from dataclasses import dataclass


@dataclass
class P11HadParticipant(P12OccurredInThePresenceOf):
    """
Scope note:
This property describes the active or passive participation of instances of E39 Actors in an instance of E5 Event.

It documents known events in which an instance of E39 Actor has participated during the course of that actor&#8217;s life or history. The instances of E53 Place and E52 Time-Span where and when these events happened provide us with constraints about the presence of the related instances of E39 Actor in the past. Collective actors, i.e., instances of E74 Group, may physically participate in events via their representing instances of E21 Persons only. The participation of multiple actors in an event is most likely an indication of their acquaintance and interaction.
The property implies that the actor was involved in the event but does not imply any causal relationship. For instance, someone having been portrayed can be said to have participated in the creation of the portrait.


Examples:
- Napoleon (E21) participated in The Battle of Waterloo (E7)
- Maria (E21) participated in Photographing of Maria (E7)


In First Order Logic:
P11(x,y) &#8835; E5(x)
P11(x,y) &#8835; E39(y)
P11(x,y) &#8835; P12(x,y)
    """

    URI = "http://erlangen-crm.org/current/P11_had_participant"
