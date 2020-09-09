from dataclasses import dataclass


@dataclass
class P161HasSpatialProjection:
    """
Scope note:
This property associates an instance of an instance of E92 Spacetime Volume with an instance of E53 Place that is the result of the spatial projection of the instance of the E92 Spacetime Volume on a reference space.

In general there can be more than one useful reference space (for reference space see P156 occupies and P157 is at rest relative to) to describe the spatial projection of a spacetime volume, for example, in describing a sea battle, the difference between the battle ship and the seafloor as reference spaces. Thus it can be seen that the projection is not unique.

The spatial projection is the actual spatial coverage of a spacetime volume, which normally has fuzzy boundaries except for instances of E92 Spacetime Volumes which are geometrically defined in the same reference system as the range of this property are an exception to this and do not have fuzzy boundaries. Modelling explicitly fuzzy spatial projections serves therefore as a common topological reference of different spatial approximations rather than absolute geometric determination, for instance for relating outer or inner spatial boundaries for the respective spacetime volumes.

In case the domain of an instance of P161 has spatial projection is an instance of E4 Period, the spatial projection describes all areas that period was ever present at, for instance, the Roman Empire. 

This property is part of the fully developed path from E18 Physical Thing through P196 defines, E92 Spacetime Volume, P161 has spatial projection, which in turn is implied by P156 occupies (is occupied by).

This property is part of the fully developed path from E4 Period through P161 has spatial projection,
E53 Place, P89 falls within (contains) to E53 Place, which in turn is shortcut by P7 took place at
(witnessed).


Example:
The Roman Empire P161 has spatial projection all areas ever claimed by Rome.


In First Order Logic:
P161(x,y) &#8835; E92(x)
P161(x,y) &#8835; E53(y)
    """

    URI = "http://erlangen-crm.org/current/P161_has_spatial_projection"
