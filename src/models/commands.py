"""Command."""

import logging
import time

from ..utils.utils import (
    assert_1_byte_data,
    assert_device_address,
    assert_register_address,
    assert_single_data,
    convert_register_length_to_hex,
    modbus_crc16,
)
from .common import Base_Model
from .m_type import FunctionCode

logger = logging.getLogger(__name__)


class BaseCommandModel(Base_Model):
    """
    base command models
    """

    Register_Address: str
    CMD: str = ""

    def model_post_init(self, __context: None) -> None:
        """models post init"""
        self._generate_cmd()

    def _generate_cmd(self) -> str:
        """generate format Input Read Command"""
        assert_device_address(self.Device_Address)
        return ""

    def __str__(self) -> str:
        """__str__"""
        format_str = f"{self.__class__.__name__}("
        for item in self.model_dump():
            format_str = format_str + f"{item}={self.model_dump()[item]} "
        return format_str.strip() + ")"


####################################################################################


class BaseReadCommand(BaseCommandModel):
    """Base Read Command."""

    Register_Count: int

    def _generate_cmd(self) -> str:
        """generate format Input Read Command"""
        super()._generate_cmd()
        assert_register_address(self.Register_Address)
        cmd: str = (
            f"{self.Device_Address}"
            f"{self.Function_Code.value}"
            f"{self.Register_Address}"
            f"{convert_register_length_to_hex(self.Register_Count)}"
        )
        self.Crc16 = modbus_crc16(cmd)
        self.CMD = cmd + self.Crc16
        return self.CMD


class SwitchReadCommand(BaseReadCommand):
    """SwitchReadCommand."""

    Function_Code: FunctionCode = FunctionCode.SwitchRead


class InputReadCommand(BaseReadCommand):
    """StateReadCommand."""

    Function_Code: FunctionCode = FunctionCode.InputRead


class StateReadCommand(BaseReadCommand):
    """StateReadCommand."""

    Function_Code: FunctionCode = FunctionCode.StateRead


####################################################################################


class BaseWriteCommand(BaseCommandModel):
    """Base Write Command."""

    Data: str
    Register_Address: str

    def _generate_cmd(self) -> str:
        """generate format Input write Command"""
        super()._generate_cmd()
        assert_register_address(self.Register_Address)
        return ""


class SingleWriteCommand(BaseWriteCommand):
    """SingleWriteCommand."""

    Function_Code: FunctionCode = FunctionCode.SingleWrite
    Register_Count: str = "01"

    def _generate_cmd(self) -> str:
        """generate format Input write Command"""
        super()._generate_cmd()
        assert_single_data(self.Data)
        cmd: str = (
            f"{self.Device_Address}"
            f"{self.Function_Code.value}"
            f"{self.Register_Address}"
            f"{self.Register_Count}"
            f"{self.Data}"
        )
        self.Crc16 = modbus_crc16(cmd)
        self.CMD = cmd + self.Crc16
        return self.CMD


class SetupWriteCommand(BaseWriteCommand):
    """SetupWriteCommand."""

    Function_Code: FunctionCode = FunctionCode.SetupWrite
    Register_Count: str = "01"
    Byte_Count: str = "01"

    def _generate_cmd(self) -> str:
        """generate format Input write Command"""
        super()._generate_cmd()
        assert_1_byte_data(self.Data)
        cmd: str = (
            f"{self.Device_Address}"
            f"{self.Function_Code.value}"
            f"{self.Register_Address}"
            f"{self.Register_Count}"
            f"{self.Byte_Count}"
            f"{self.Data}"
        )
        self.Crc16 = modbus_crc16(cmd)
        self.CMD = cmd + self.Crc16
        return self.CMD


class MultiWriteCommand(BaseWriteCommand):
    """MultiWriteCommand."""

    Function_Code: FunctionCode = FunctionCode.MultiWrite

    def __get_register_count(self) -> str:
        """get register count."""
        _length: int = len(self.Data)
        if _length % 4 != 0:
            msg: str = f"Multi Write Data Format Error {self.Data}"
            logger.error(msg)
            raise ValueError(msg)
        return convert_register_length_to_hex(int(_length / 4))

    def __get_bytes_number(self) -> str:
        """get bytes count."""
        _length: int = len(self.Data)
        if _length % 2 != 0:
            msg: str = f"Multi Write Data Format Error {self.Data}"
            logger.error(msg)
            raise ValueError(msg)

        hex_char: str = hex(int(_length / 2)).replace("0x", "")
        start_time: float = time.time()
        while len(hex_char) != 2:
            if time.time() - start_time > 1:
                break
            hex_char = "0" + hex_char
        return hex_char.upper()

    def _generate_cmd(self) -> str:
        """generate format Input write Command"""
        super()._generate_cmd()
        cmd: str = (
            f"{self.Device_Address}"
            f"{self.Function_Code.value}"
            f"{self.Register_Address}"
            f"{self.__get_register_count()}"
            f"{self.__get_bytes_number()}"
            f"{self.Data}"
        )
        self.Crc16 = modbus_crc16(cmd)
        self.CMD = cmd + self.Crc16
        return self.CMD
