from dataclasses import dataclass


@dataclass
class P147Curated:
    """
Scope note:
This property associates an instance of E87 Curation Activity with the instance of E78 Curated Holdingwith that is subject of that curation activity following some implicit or explicit curation plan.


Examples:
- The activities (E87) by the Benaki Museum curated the acquisition of dolls and games of urban and folk manufacture dating from the 17th to the 20th century, from England, France and Germany for the "Toys, Games and Childhood Collection (E78) of the Museum
- The activities (E87) of the Historical Museum of Crete, Heraklion, Crete, curated the development of the permanent Numismatic Collection (E78)
- The activities (E87) by Mikael Heggelund Foslie curated the Mikael Heggelund Foslie's coralline red algae Herbarium


In First Order Logic:
P147(x,y) &#8835; E87(x)
P147(x,y) &#8835; E78(y)
    """

    URI = "http://erlangen-crm.org/current/P147_curated"
