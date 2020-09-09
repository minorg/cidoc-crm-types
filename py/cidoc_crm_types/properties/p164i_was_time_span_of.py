from .p160i_is_temporal_projection_of import P160iIsTemporalProjectionOf
from dataclasses import dataclass


@dataclass
class P164iWasTimeSpanOf(P160iIsTemporalProjectionOf):
    URI = "http://erlangen-crm.org/current/P164i_was_time-span_of"
