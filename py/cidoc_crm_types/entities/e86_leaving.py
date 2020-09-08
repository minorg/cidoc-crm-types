from .e7_activity import E7Activity
from dataclasses import dataclass


@dataclass
class E86Leaving(E7Activity):
    """
Scope note:
This class comprises the activities that result in an instance of E39 Actor to be disassociated from an instance of E74 Group. This class does not imply initiative by either party. It may be the initiative of a third party.

Typical scenarios include the termination of membership in a social organisation, ending the employment at a company, divorce, and the end of tenure of somebody in an official position.


Examples:
- The end of Sir Isaac Newton?s duty as Member of Parliament for the University of Cambridge to the Convention Parliament in 1702 (Gleick, 2003)
- George Washington?s leaving office in 1797 (Jones, 1979)
- The implementation of the treaty regulating the termination of Greenland?s membership in EU between EU, Denmark and Greenland February 1. 1985


In First Order Logic:
E86(x) ? E7(x)
    """

    _typename: str = 'E86Leaving'
