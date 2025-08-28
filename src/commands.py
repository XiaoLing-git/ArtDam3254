"""Command."""

from typing import Any

from .m_type import FunctionCode
from .models import Base_Model
from .utils import (
    assert_device_address,
    assert_function_code,
    assert_register_address,
    convert_register_length_to_hex,
    modbus_crc16,
)


class BaseCommandModel(Base_Model):
    """
    base command model
    """

    Register_Address: str


class InputReadCommand(BaseCommandModel):
    """InputReadCommand."""

    def __init__(self, /, **data: Any) -> None:
        """InputReadCommand init."""
        super().__init__(**data)
        self.__generate_cmd()

    Function_Code: FunctionCode = FunctionCode.InputRead
    Register_Count: int

    def __generate_cmd(self) -> str:
        """generate format Input Read Command"""
        assert_device_address(self.Device_Address)
        assert_function_code(self.Function_Code)
        assert_register_address(self.Register_Address)
        cmd: str = (
            f"{self.Device_Address}"
            f"{self.Function_Code.value}"
            f"{self.Register_Address}"
            f"{convert_register_length_to_hex(self.Register_Count)}"
        )
        self.Crc16 = modbus_crc16(cmd)
        cmd = cmd + self.Crc16
        return cmd

    def __str__(self) -> str:
        """__str__"""
        return self.__generate_cmd()


class StateReadCommand(BaseCommandModel):
    """StateReadCommand."""

    Function_Code: FunctionCode = FunctionCode.StateRead
    Register_Count: int


class SingleWriteCommand(BaseCommandModel):
    """SingleWriteCommand."""

    Function_Code: FunctionCode = FunctionCode.SingleWrite
    Data: str


class MultiWriteCommand(BaseCommandModel):
    """MultiWriteCommand."""

    Function_Code: FunctionCode = FunctionCode.MultiWrite
    Register_Address: str
    Data: str
