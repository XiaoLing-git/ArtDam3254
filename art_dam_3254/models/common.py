"""models."""

from pydantic import BaseModel

from .m_type import FunctionCode

Serial_Connection_Log_Output: bool = False

Serial_Write_Read_Log_Output: bool = False

Serial_Write_Read_Log_Clean_Output: bool = False

Modbus_Crc16_Log_Output: bool = False

Base_Driver_Log_Output: bool = True


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
