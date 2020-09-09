from dataclasses import dataclass


@dataclass
class P69HasAssociationWith:
    """
Scope note:
This property generalises relationships like whole-part, sequence, prerequisite or inspired by between instances of E29 Design or Procedure. Any instance of E29 Design or Procedure may be associated with other designs or procedures. The property is considered to be symmetrical unless otherwise indicated by P69.1 has type.
The P69.1 has type property of P69 has association with allows the nature of the association to be specified reading from domain to range; examples of types of association between instances of E29 Design or Procedure include: has part, follows, requires, etc. 
The property can typically be used to model the decomposition of the description of a complete workflow into a series of separate procedures.
This property is transitive.


Examples:
- Procedure for glass blowing (E29) has association with procedure for glass heating (E29) 
- The set of instructions for performing Macbeth in Max Reinhardt's production in 1916 in Berlin at Deutsches Theater (E29) has association with the scene design drawing by Ernst Stern reproduced at http://www.glopad.org/pi/fr/record/digdoc/1003814 (E29) has type has part (E55) 
- Preparation of parchment (E29) has association with soaking and unhairing of skin (E29) has type 'has part' (E55). Preparation of parchment (E29) has association with stretching of skin (E29) has type 'has part' (E55). Stretching of skin (E29) has association with soaking and unhairing of skin (E29) has type 'follows' (E55).
- The plan for reassembling the temples at Abu Simbel (E29) has association with the plan for storing and transporting the blocks (E29) has type 'follows' (E55)'.


In First Order Logic:
P69 (x,y) &#8835; E29(x)
P69 (x,y) &#8835; E29(y)
P69(x,y,z) &#8835; [P69(x,y) &#8743; E55(z)]
P69(x,y) &#8835;P69(y,x)
    """

    URI = "http://erlangen-crm.org/current/P69_has_association_with"
