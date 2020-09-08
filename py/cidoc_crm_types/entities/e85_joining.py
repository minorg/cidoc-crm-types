from .e7_activity import E7Activity
from dataclasses import dataclass


@dataclass
class E85Joining(E7Activity):
    """
Scope note:
This class comprises the activities that result in an instance of E39 Actor becoming a member of an instance of E74 Group. This class does not imply initiative by either party. It may be the initiative of a third party.

Typical scenarios include becoming a member of a social organisation, becoming employee of a company, marriage, the adoption of a child by a family and the inauguration of somebody into an official position. 


Examples:
- The election of Sir Isaac Newton as Member of Parliament for the University of Cambridge to the Convention Parliament of 1689 (Gleick,2003)
- The inauguration of Mikhail Sergeyevich Gorbachev as leader of the Union of Soviet Socialist Republics (USSR) in 1985 (Butson, 1986)
- The implementation of the membership treaty between EU and Denmark January 1. 1993


In First Order Logic:
E85(x) ? E7(x)
    """

    __typename: str = 'E85Joining'
