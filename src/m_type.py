"""m_type.py"""

from __future__ import annotations

from enum import Enum

from src.errors import FunctionCodeNotExistException, ModeNotExistException
from src.register_address import (
    Analog_Channel_1_Address,
    Analog_Channel_1_Range,
    Analog_Channel_2_Address,
    Analog_Channel_2_Range,
    Analog_Channel_3_Address,
    Analog_Channel_3_Range,
    Analog_Channel_4_Address,
    Analog_Channel_4_Range,
    Analog_Channel_Address,
)


class BaseEnum(Enum):
    """base Enum statement."""


class FunctionCode(BaseEnum):
    """base function code statement."""

    SwitchRead = "02"
    StateRead = "03"
    InputRead = "04"
    SingleWrite = "06"
    SwitchControl = "0F"
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

AnalogChannelMapRangeAddress: dict[AnalogChannel, int] = {
    AnalogChannel.ch1: Analog_Channel_1_Range,
    AnalogChannel.ch2: Analog_Channel_2_Range,
    AnalogChannel.ch3: Analog_Channel_3_Range,
    AnalogChannel.ch4: Analog_Channel_4_Range,
}


class AnalogInputRange(BaseEnum):
    """Analog Input Range"""

    V_0__5 = "000D"
    V_1__5 = "0082"
    V_0__2_5 = "000F"
    MA_0_20 = "000B"
    MA_4_20 = "000C"

    @classmethod
    def get_all_values(cls) -> list[AnalogInputRange]:
        """get all enum instance."""
        return list(cls.__members__.values())

    @classmethod
    def map_value(cls, target: str) -> AnalogInputRange:
        """map value to enum instance."""
        for item in AnalogInputRange.get_all_values():
            if target == item.value:
                return item
        raise ModeNotExistException(f"{target} not existed in {cls.get_all_values()}")


AnalogInputRangeMapValue: dict[AnalogInputRange, tuple[float, float, str]] = {
    AnalogInputRange.V_0__5: (0, 5, "V"),
    AnalogInputRange.V_1__5: (1, 5, "V"),
    AnalogInputRange.V_0__2_5: (0, 2.5, "V"),
    AnalogInputRange.MA_0_20: (0, 20, "mA"),
    AnalogInputRange.MA_4_20: (4, 5, "mA"),
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


class SwitchStatus(BaseEnum):
    """
    SwitchStatus.
    """

    On = "01"
    Off = "00"

    @classmethod
    def get_all_values(cls) -> list[SwitchStatus]:
        """get all enum instance."""
        return list(cls.__members__.values())

    @classmethod
    def map_value(cls, target: str) -> SwitchStatus:
        """map value to enum instance."""
        for item in cls.get_all_values():
            if target == item.value:
                return item
        raise ModeNotExistException(f"{target} not existed in {cls.get_all_values()}")
