from .p67_refers_to import P67RefersTo
from dataclasses import dataclass


@dataclass
class P70Documents(P67RefersTo):
    """
Scope note:
This property describes the CRM Entities documented as instances of E31 Document.
Documents may describe any conceivable entity, hence the link to the highest-level entity in the CIDOC CRM class hierarchy. This property is intended for cases where a reference is regarded as making a proposition about reality. This may be of a documentary character, in the scholarly or scientific sense, or a more general statement


Examples:
- the British Museum catalogue (E31) documents the British Museum's Collection (E78)


In First Order Logic:
P70 (x,y) &#8835; E31(x)
P70 (x,y) &#8835; E1(y)
P70(x,y) &#8835; P67(x,y)
    """

    URI = "http://erlangen-crm.org/current/P70_documents"
