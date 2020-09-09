from dataclasses import dataclass


@dataclass
class E1CRMEntity:
    """
This class comprises all things in the universe of discourse of the CIDOC Conceptual Reference Model.

It is an abstract concept providing for three general properties:
1. Identification by name or appellation, and in particular by a preferred identifier
2. Classification by type, allowing further refinement of the specific subclass an instance belongs to
3. Attachment of free text and other unstructured data for the expression of anything not captured by formal properties

All other classes within the CIDOC CRM are directly or indirectly specialisations of E1 CRM Entity. 


Examples:
- the earthquake in Lisbon 1755 (E5) (Chester, 2001)


In First Order Logic: 
E1(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E1_CRM_Entity"
