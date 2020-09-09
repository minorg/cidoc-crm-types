from .e24_physical_human_made_thing import E24PhysicalHumanMadeThing
from .e26_physical_feature import E26PhysicalFeature
from dataclasses import dataclass


@dataclass
class E25HumanMadeFeature(E26PhysicalFeature, E24PhysicalHumanMadeThing):
    """
Scope note:
This class comprises physical features that are purposely created by human activity, such as scratches, artificial caves, artificial water channels, etc. In particular, it includes the information encoding features on mechanical or digital carriers.

No assumptions are made as to the extent of modification required to justify regarding a feature as human-made. For example, rock art or even &#8220;cup and ring&#8221; carvings on bedrock are regarded as types of E25 Human-Made Feature.


Examples:
- the Manchester Ship Canal (Famie, 1980)
- Michael Jackson&#8217;s nose following plastic surgery
- The laser-readable &#8220;pits&#8221; engraved June 2014 on Martin Doerr&#8217;s CD-R, copying songs of Edith Piaf&#8217;s.
- The carved letters on the Rosetta Stone


In First Order Logic:
E25(x) &#8835; E26(x)
E25(x) &#8835; E24(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E25_Human-Made_Feature"
