from enum import Enum, auto


class PropertyType(Enum):
    DATATYPE = auto()
    FUNCTIONAL = auto()
    INVERSE_FUNCTIONAL = auto()
    OBJECT = auto()
    SYMMETRIC = auto()
    TRANSITIVE = auto()
