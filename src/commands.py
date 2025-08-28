"""Command."""

from .m_type import FunctionCode
from .models import Base_Model


class BaseCommandModel(Base_Model):
    """
    base command model
    """


class InputReadCommand(BaseCommandModel):
    """InputReadCommand."""

    Function_Code: FunctionCode = FunctionCode.InputRead
    Register_Address: str
    Register_Count: int


class StateReadCommand(BaseCommandModel):
    """StateReadCommand."""

    Function_Code: FunctionCode = FunctionCode.StateRead
    Register_Address: str
    Register_Count: int


class SingleWriteCommand(BaseCommandModel):
    """SingleWriteCommand."""

    Function_Code: FunctionCode = FunctionCode.SingleWrite
    Register_Address: str
    Data: str


class MultiWriteCommand(BaseCommandModel):
    """MultiWriteCommand."""

    Function_Code: FunctionCode = FunctionCode.MultiWrite
    Register_Address: str
    Length: str
    Data: str
