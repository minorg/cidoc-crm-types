from dataclasses import dataclass


@dataclass
class P67RefersTo:
    """
Scope note:
This property documents that an instance of E89 Propositional Object makes a statement about an instance of E1 CRM Entity. P67 refers to (is referred to by) has the P67.1 has type link to an instance of E55 Type. This is intended to allow a more detailed description of the type of reference. This differs from P129 is about (is subject of), which describes the primary subject or subjects of the instance of E89 Propositional Object.


Examples:
- the eBay auction listing for 4 July 2002 (E73) refers to silver cup 232 (E22) has type item for sale (E55)


In First Order Logic:
P67(x,y) &#8835; E89(x)
P67(x,y) &#8835; E1(y)
P67(x,y,z) &#8835; [P67(x,y) &#8743; E55(z)]
    """

    URI = "http://erlangen-crm.org/current/P67_refers_to"
