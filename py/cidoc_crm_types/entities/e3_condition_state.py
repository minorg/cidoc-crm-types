from .e2_temporal_entity import E2TemporalEntity
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E3ConditionState(E2TemporalEntity):
    """
Scope note:
This class comprises the states of objects characterised by a certain condition over a time-span.

An instance of this class describes the prevailing physical condition of any material object or feature during a specific E52 Time Span. In general, the time-span for which a certain condition can be asserted may be shorter than the real time-span, for which this condition held. The nature of that condition can be described using  P2 has type. For example, the E3 Condition State "condition of the SS Great Britain between 22 September 1846 and 27 August 1847" can be characterized as E55 Type "wrecked".


Examples:
-  the "reconstructed" state of the ?Amber Room? in Tsarskoje Selo from summer 2003 until now (Owen, 2009)
- the "ruined" state of Peterhof Palace near Saint Petersburg from 1944 to 1946 (Maddox, 2015)
- the state of my turkey in the oven at 14:30 on 25 December, 2002 (P2 has type: E55 Type ?still not cooked?)
- the topography of the leaves of Sinai Printed Book 3234.2361 on the 10th of July 2007 (described as: of type "cockled")


In First Order Logic:
E3(x) ? E2(x)
    """

    P35_was_identified_by: Tuple[object, ...] = ()  # Range: E1CRMEntity
    P44_is_condition_of: Tuple[object, ...] = ()  # Range: E18PhysicalThing
    P5_consists_of: Tuple[object, ...] = ()  # Range: E3ConditionState
    P5_forms_part_of: Tuple[object, ...] = ()  # Range: E3ConditionState
    _typename: str = 'E3ConditionState'
