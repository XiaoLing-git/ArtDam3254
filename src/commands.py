from enum import Enum


class FunctionCode(Enum):
    """base function code statement."""

    InputRead = "04"
    StateRead = "03"
    SingleWrite = "06"
    MultiWrite = "10"


class AnalogChannelAddress(Enum):
    """Analog channel read address."""

    all = "00000004"
    ch1 = "00000001"
    ch2 = "00010001"
    ch3 = "00020001"
    ch4 = "00030001"


class IoMode(Enum):
    """Pin IO mode options."""

    Normal = "01"
    RiseEdge = "02"
    FallEdge = "03"
    Count = "04"
