from .e18_physical_thing import E18PhysicalThing
from .e71_man_made_thing import E71ManMadeThing
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E24PhysicalManMadeThing(E18PhysicalThing, E71ManMadeThing):
    """
Scope note:
This class comprises all persistent physical items of any size that are purposely created by human activity. This class comprises, besides others, Human-Made objects, such as a swords, and Human-Made features, such as rock art. For example, a ?cup and ring? carving on bedrock is regarded as instance of E24 Physical Human-Made Thing.

Instances of Human-Made thing may be the result of modifying pre-existing physical things, preserving larger parts or most of the original matter and structure, which poses the question if they are new or even Human-Made, the respective interventions of production made on such original material should be obvious and sufficient to regard that the product has a new, distinct identity and intended function and is human-made. Substantial continuity of the previous matter and structure in the new product can be documented by describing the production process also as instance of E81 Transformation.

Whereas interventions of conservation and repair are not regarded to produce a new Human-Made thing, the results of preparation of natural history specimen that substantially change their natural or original state should be regarded as physical Human-Made things, including the uncovering of petrified biological features from a solid piece of stone. On the other side, scribbling a museum number on a natural object should not be regarded to make it Human-Made. This notwithstanding, parts, sections, segments, or features of a physical Human-Made thing may continue to be non-Human-Made and preserved during the production process, for example natural pearls used as a part of an eardrop.


Examples:
- the Forth Railway Bridge (E22) (The Forth Railway Bridge centenary 1890-1990 ICE Proceedings, 1990, Vol.88(6), pp.1079-1107.
- the Channel Tunnel (E25) (Holliday, I., Marcou, G., and Vickerman, R. W., 1991)
- the Historical Collection of the Museum Benaki in Athens (E78) (Georgoula, E., 2005)
- the Rosetta Stone (E22)
- my paperback copy of Crime & Punishment (E22) (fictitious)
- the computer disk at ICS-FORTH that stores the canonical Definition of the CIDOC CRM v.3.2 (E22)
- my empty DVD disk (E22) (fictitious)

In First Order Logic:
E24(x) ? E18(x)
E24(x) ? E71(x)
    """

    P62_depicts: Tuple[object, ...] = ()  # Range: E1CRMEntity
    _typename: str = 'E24PhysicalManMadeThing'
