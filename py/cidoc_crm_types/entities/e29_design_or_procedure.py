from .e73_information_object import E73InformationObject
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E29DesignorProcedure(E73InformationObject):
    """
Scope note:
This class comprises documented plans for the execution of actions in order to achieve a result of a specific quality, form or contents. In particular, it comprises plans for deliberate human activities that may result in new instances of E71 Human-Made Thing or for shaping or guiding the execution of an instance of E7 Activity.

Instances of E29 Design or Procedure can be structured in parts and sequences or depend on others. This is modelled using P69 has association with (is associated with): E29 Design or Procedure 

Designs or procedures can be seen as one of the following:
1. A schema for the activities it describes
2. A schema of the products that result from their application.
3. An independent intellectual product that may have never been applied, such as Leonardo da Vinci?s famous plans for flying machines.

Because designs or procedures may never be applied or only partially executed, the CIDOC CRM models a loose relationship between the plan and the respective product.


Examples:
- the ISO standardisation procedure
- the musical notation of Beethoven's "Ode to Joy"
- the architectural drawings for the K?lner Dom in Cologne, Germany
- The drawing on the folio 860 of the Codex Atlanticus from Leonardo da Vinci, 1486-1490, kept in the Biblioteca Ambrosiana in Milan


In First Order Logic:
E29(x) ? E73(x)
    """

    P187i_is_production_plan_for: Tuple[object, ...] = ()  # Range: E99ProductType
    P69_has_association_with: Tuple[object, ...] = ()  # Range: E29DesignorProcedure
    P69_is_associated_with: Tuple[object, ...] = ()  # Range: E29DesignorProcedure
    __typename: str = 'E29DesignorProcedure'
