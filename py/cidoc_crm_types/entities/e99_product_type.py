from .e55_type import E55Type
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E99ProductType(E55Type):
    """
Scope note:
This classes comprises types that stand as the models for instances of E22 Human-Made Object that are produced as the result of production activities using plans exact enough to result in one or more series of uniform, functionally and aesthetically identical and interchangeable items. The product type is the intended ideal form of the manufacture process. It is typical of instances of E22 that conform to an instance of E99 Product Type that its component parts are interchangeable with component parts of other instances of E22 made after the model of the same instance of E99. Frequently, the uniform production according to a given instance of E99 Product Type is achieved by creating individual tools, such as moulds or print Definition of the CIDOC Conceptual Reference Model version 6.2.8 45 plates that are themselves carriers of the design of the product type. Modern tools may use the flexibility of electronically controlled devices to achieve such uniformity. The product type itself, i.e., the potentially unlimited series of aesthetically equivalent items, may be the target of artistic design, rather than the individual object. In extreme cases, only one instance of a product type may have been produced, such as in a "print on demand" process which was only triggered once. However, this should not be confused with industrial prototypes, such as car prototypes, which are produced prior to the production line being set up, or test the production line itself.


Examples:
- Volkswagen Type 11 (Beetle)
- Dragendorff 54 samian vessel
- 1937 Edward VIII brass threepenny bit
- Qin Crossbow trigger un-notched Part B (Bg2u)
- Nokia Cityman 1320 (The first Nokia mobile phone)


In First Order Logic:
E99(x) ? E55(x)
    """

    P186_produced_thing_of_product_type: Tuple[object, ...] = ()  # Range: E12Production
    P187_has_production_plan: Tuple[object, ...] = ()  # Range: E29DesignorProcedure
    P188_requires_production_tool: Tuple[object, ...] = ()  # Range: E19PhysicalObject
    __typename: str = 'E99ProductType'
