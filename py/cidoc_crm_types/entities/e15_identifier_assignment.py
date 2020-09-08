from .e13_attribute_assignment import E13AttributeAssignment
from dataclasses import dataclass


@dataclass
class E15IdentifierAssignment(E13AttributeAssignment):
    """
Scope note:
This class comprises activities that result in the allocation of an identifier to an instance of E1 CRM Entity. Instances of E15 Identifier Assignment may include the creation of the identifier from multiple constituents, which themselves may be instances of E41 Appellation. The syntax and kinds of constituents to be used may be declared in a rule constituting an instance of E29 Design or Procedure. 

Examples of such identifiers include Find Numbers, Inventory Numbers, uniform titles in the sense of librarianship and Digital Object Identifiers (DOI). Documenting the act of identifier assignment and deassignment is especially useful when objects change custody or the identification system of an organization is changed. In order to keep track of the identity of things in such cases, it is important to document by whom, when and for what purpose an identifier is assigned to an item.

The fact that an identifier is a preferred one for an organisation can be expressed by using the property E1 CRM Entity. P48 has preferred identifier (is preferred identifier of): E42 Identifier. It can better be expressed in a context independent form by assigning a suitable E55 Type, such as ?preferred identifier assignment?, to the respective instance of E15 Identifier Assignment via the P2 has type property.


Examples:
- Replacement of the inventory number TA959a by GE34604 for a 17th century lament cloth at the Museum Benaki, Athens
- Assigning the author-uniform title heading ?Goethe, Johann Wolfgang von, 1749-1832. Faust. 1. Theil.? for the respective work
- On June 1, 2001 assigning the personal name heading ?Guillaume, de Machaut, ca. 1300-1377? to Guillaume de Machaut


In First Order Logic:
E15(x) ? E13(x)
    """

    _typename: str = 'E15IdentifierAssignment'
