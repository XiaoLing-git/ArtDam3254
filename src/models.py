"""model."""

from pydantic import BaseModel

from src.m_type import FunctionCode

Serial_Write_Read_Log_Output: bool = True

Modbus_Crc16_Log_Output: bool = False


class Base_Model(BaseModel):  # type: ignore[misc]
    """
    base data mode
    :param Device_Address
    :param Function_Code
    :param Crc16
    """

    Device_Address: str
    Function_Code: FunctionCode
    Crc16: str | None = None
