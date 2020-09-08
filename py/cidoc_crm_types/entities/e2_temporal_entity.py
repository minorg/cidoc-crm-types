from .e1_crm_entity import E1CRMEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E2TemporalEntity(E1CRMEntity):
    """
Scope note:
This class comprises all phenomena, such as the instances of E4 Periods and E5 Events, which happen over a limited extent in time. This extent in time must be contiguous, i.e., without gaps. In case the defining kinds of phenomena for an instance of E2 Temporal Entity cease to happen, and occur later again at another time, we regard that the former instance of E2 Temporal Entity has ended and a new instance has come into existence. In more intuitive terms, the same event cannot happen twice.

In some contexts, such phenomena are also called perdurants. This class is disjoint from E77 Persistent Item and is an abstract class that typically has no direct instances. E2 Temporal Entity is specialized into E4 Period, which applies to a particular geographic area (defined with a greater or lesser degree of precision), and E3 Condition State, which applies to instances of E18 Physical Thing.


Examples:
- Bronze Age (E4) (Childe, 1963)
- the earthquake in Lisbon 1755 (E5) (Chester, 2001)
- the Peterhof Palace near Saint Petersburg being in ruins from 1944 ? 1946 (E3) (Maddox, 2015)


In First Order Logic:
E2(x) ? E1(x)
    """

    P173_starts_before_or_at_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P174_ends_after_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P174_starts_before_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P175_starts_before_or_with_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P175i_starts_after_or_with_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P176_starts_before_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P176i_starts_after_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P182_ends_befort_or_at_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P182i_starts_after_or_with_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P183_ends_before_the_start_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P183i_starts_after_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P184_ends_before_or_with_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P184_ens_before_or_with_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P185_ends_before_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P185i_ends_after_the_end_of: Tuple[object, ...] = ()  # Range: E2TemporalEntity
    P4_has_time_span: Tuple[object, ...] = ()  # Range: E52TimeSpan
    __typename: str = 'E2TemporalEntity'
