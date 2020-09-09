from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass


@dataclass
class E92SpacetimeVolume(E1CRMEntity):
    """
Scope note:
This class comprises 4 dimensional point sets (volumes) in physical spacetime (in contrast to mathematical models of it) regardless their true geometric forms. They may derive their identity from being the extent of a material phenomenon or from being the interpretation of an expression defining an extent in spacetime. Intersections of instances of E92 Spacetime Volume, E53 Place and E52 Timespan are also regarded as instances of E92 Spacetime Volume. An instance of E92 Spacetime Volume is either contiguous or composed of a finite number of contiguous subsets. Its boundaries may be fuzzy due to the properties of the phenomena it derives from or due to the limited precision up to which defining expression can be identified with a real extent in spacetime. The duration of existence of an instance of E92 Spacetime Volume is its projection on time.


Examples:
- the&#160;spacetime&#160;Volume&#160;of&#160;the&#160;Event&#160;of&#160;Ceasars&#160;murder&#160;
- the&#160;spacetime&#160;Volume&#160;where&#160;and&#160;when&#160;the&#160;carbon&#160;14&#160;dating&#160;of&#160;the&#160;"Schoeninger&#160;Speer&#160;II"&#160;in&#160;1996 &#160;took&#160;place&#160;
- the&#160;spatio&#8208;temporal&#160;trajectory&#160;of&#160;the&#160;H.M.S.&#160;Victory&#160;from&#160;its&#160;building&#160;to&#160;its&#160;actual&#160;location
- the&#160;spacetime&#160;volume&#160;defined&#160;by&#160;a&#160;polygon&#160;approximating&#160;the&#160;Danube&#160;river&#160;flood&#160;in&#160;Austria&#160;between&#160;6th&#160;and&#160;9th&#160;of&#160;August&#160;2002


In First Order Logic:
E92(x) &#8835; E1(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E92_Spacetime_Volume"
