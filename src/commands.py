"""Command."""

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


class AnalogChannelRangeAddress(Enum):
    """Analog channel range read address."""

    all = "00C80004"
    ch1 = "00C80001"
    ch2 = "00C90001"
    ch3 = "00CA0001"
    ch4 = "00CB0001"


class InputIoMode(Enum):
    """Pin input IO mode options."""

    Normal = "01"
    RiseEdge = "02"
    FallEdge = "03"
    Count = "04"


class OutputIoMode(Enum):
    """Pin output IO mode options."""

    Normal = "01"
    RiseEdgeDelay = "02"
    FallEdgeDelay = "03"
    Pulse = "04"
