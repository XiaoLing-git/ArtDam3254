"""m_type.py"""

from __future__ import annotations

from enum import Enum

from src.errors import FunctionCodeNotExistException, ModeNotExistException
from src.register_address import (
    Analog_Channel_1_Address,
    Analog_Channel_2_Address,
    Analog_Channel_3_Address,
    Analog_Channel_4_Address,
    Analog_Channel_Address,
)


class BaseEnum(Enum):
    """base Enum statement."""


class FunctionCode(BaseEnum):
    """base function code statement."""

    InputRead = "04"
    StateRead = "03"
    SingleWrite = "06"
    MultiWrite = "10"

    @classmethod
    def get_all_values(cls) -> list[FunctionCode]:
        """get all enum instance."""
        return list(cls.__members__.values())

    @classmethod
    def map_value(cls, target: str) -> FunctionCode:
        """map value to enum instance."""
        for item in FunctionCode.get_all_values():
            if target == item.value:
                return item
        raise FunctionCodeNotExistException(f"{target} not existed in {cls.get_all_values()}")


class AnalogChannel(BaseEnum):
    """Analog channel."""

    all = 0
    ch1 = 1
    ch2 = 2
    ch3 = 3
    ch4 = 4


AnalogChannelMapAddress: dict[AnalogChannel, int] = {
    AnalogChannel.all: Analog_Channel_Address,
    AnalogChannel.ch1: Analog_Channel_1_Address,
    AnalogChannel.ch2: Analog_Channel_2_Address,
    AnalogChannel.ch3: Analog_Channel_3_Address,
    AnalogChannel.ch4: Analog_Channel_4_Address,
}


class DigitalInputMode(BaseEnum):
    """Digital Signal Input Mode."""

    Normal = 1
    Low2HighLatch = 2
    High2LowLatch = 3
    Counter = 4

    @classmethod
    def get_all_values(cls) -> list[DigitalInputMode]:
        """get all enum instance."""
        return list(cls.__members__.values())

    @classmethod
    def map_value(cls, target: int) -> DigitalInputMode:
        """map value to enum instance."""
        for item in cls.get_all_values():
            if target == item.value:
                return item
        raise ModeNotExistException(f"{target} not existed in {cls.get_all_values()}")


class DigitalOutputMode(BaseEnum):
    """Digital Signal Output Mode."""

    Normal = 1
    Low2HighDelay = 2
    High2LowDelay = 3
    Pulse = 4

    @classmethod
    def get_all_values(cls) -> list[DigitalOutputMode]:
        """get all enum instance."""
        return list(cls.__members__.values())

    @classmethod
    def map_value(cls, target: int) -> DigitalOutputMode:
        """map value to enum instance."""
        for item in cls.get_all_values():
            if target == item.value:
                return item
        raise ModeNotExistException(f"{target} not existed in {cls.get_all_values()}")


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
