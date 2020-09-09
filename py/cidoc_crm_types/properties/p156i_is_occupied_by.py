from .p161i_is_spatial_projection_of import P161iIsSpatialProjectionOf
from dataclasses import dataclass


@dataclass
class P156iIsOccupiedBy(P161iIsSpatialProjectionOf):
    URI = "http://erlangen-crm.org/current/P156i_is_occupied_by"
