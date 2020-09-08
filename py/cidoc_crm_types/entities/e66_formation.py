from .e63_beginning_of_existence import E63BeginningofExistence
from .e7_activity import E7Activity
from dataclasses import dataclass


@dataclass
class E66Formation(E63BeginningofExistence, E7Activity):
    """
Scope note: 
This class comprises events that result in the formation of a formal or informal E74 Group of people, such as a club, society, association, corporation or nation.

E66 Formation does not include the arbitrary aggregation of people who do not act as a collective. The formation of an instance of E74 Group does not require that the group is populated with members at the time of formation. In order to express the joining of members at the time of formation, the respective activity should be simultaneously an instance of both E66 Formation and E85 Joining.


Examples:
- the formation of the CIDOC CRM Special Interest Group
- the formation of the Soviet Union (Pipes, 1964)
- the conspiring of the murderers of Caesar (Irwin, 1935)


In First Order Logic:
E66(x) ? E7(x)
E66(x) ? E63(x)
    """


