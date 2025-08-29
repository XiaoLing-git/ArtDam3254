"""m_type.py"""

from __future__ import annotations

from enum import Enum

from src.errors import FunctionCodeNotExistException


class BaseEnum(Enum):
    """base Enum statement."""

    @classmethod
    def get_all_values(cls) -> list[BaseEnum]:
        """get all enum instance."""
        return list(cls.__members__.values())

    @classmethod
    def map_value(cls, target: str) -> BaseEnum:
        """map value to enum instance."""
        for item in FunctionCode.get_all_values():
            if target == item.value:
                return item
        raise FunctionCodeNotExistException(f"{target} not existed in {cls.get_all_values()}")


class FunctionCode(BaseEnum):
    """base function code statement."""

    InputRead = "04"
    StateRead = "03"
    SingleWrite = "06"
    MultiWrite = "10"


class AnalogChannelAddress(BaseEnum):
    """Analog channel read address."""

    all = "00000004"
    ch1 = "00000001"
    ch2 = "00010001"
    ch3 = "00020001"
    ch4 = "00030001"


class AnalogChannelRangeAddress(BaseEnum):
    """Analog channel range read address."""

    all = "00C80004"
    ch1 = "00C80001"
    ch2 = "00C90001"
    ch3 = "00CA0001"
    ch4 = "00CB0001"


class InputIoMode(BaseEnum):
    """Pin input IO mode options."""

    Normal = "01"
    RiseEdge = "02"
    FallEdge = "03"
    Count = "04"


class OutputIoMode(BaseEnum):
    """Pin output IO mode options."""

    Normal = "01"
    RiseEdgeDelay = "02"
    FallEdgeDelay = "03"
    Pulse = "04"
