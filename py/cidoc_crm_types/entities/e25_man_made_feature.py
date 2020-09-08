from .e24_physical_man_made_thing import E24PhysicalManMadeThing
from .e26_physical_feature import E26PhysicalFeature
from dataclasses import dataclass


@dataclass
class E25ManMadeFeature(E26PhysicalFeature, E24PhysicalManMadeThing):
    """
Scope note:
This class comprises physical features that are purposely created by human activity, such as scratches, artificial caves, artificial water channels, etc. In particular, it includes the information encoding features on mechanical or digital carriers.

No assumptions are made as to the extent of modification required to justify regarding a feature as human-made. For example, rock art or even ?cup and ring? carvings on bedrock are regarded as types of E25 Human-Made Feature.


Examples:
- the Manchester Ship Canal (Famie, 1980)
- Michael Jackson?s nose following plastic surgery
- The laser-readable ?pits? engraved June 2014 on Martin Doerr?s CD-R, copying songs of Edith Piaf?s.
- The carved letters on the Rosetta Stone


In First Order Logic:
E25(x) ? E26(x)
E25(x) ? E24(x)
    """

    __typename: str = 'E25ManMadeFeature'
