"""Command."""

from __future__ import annotations

from typing import Any

from src.m_type import FunctionCode
from src.models import Base_Model


class BaseResponseModel(Base_Model):
    """
    base command model
    """

    def __str__(self) -> str:
        """__str__"""
        format_str = f"{self.__class__.__name__}("
        for item in self.model_dump():
            format_str = format_str + f"{item}={self.model_dump()[item]} "
        return format_str.strip() + ")"


class BaseReadResponse(BaseResponseModel):
    """Base Read Response for InputReadCommand & StateReadCommand."""

    Register_Count: int
    Data: str

    @classmethod
    def response_to_model(cls, bytes_response: str) -> BaseReadResponse:
        """parse str to model."""
        results: dict[str, Any] = {
            "Device_Address": bytes_response[:2],
            "Function_Code": FunctionCode.map_value(bytes_response[2:4]),
            "Register_Count": int(bytes_response[4:6], 16),
            "Data": bytes_response[6:-4],
            "Crc16": bytes_response[-4:],
        }
        return cls(**results)


class BaseWriteResponse(BaseResponseModel):
    """Base write Response for SingleWriteCommand & MultiWriteCommand."""

    Register_Address: str


class SingleWriteResponse(BaseResponseModel):
    """Response for SingleWriteCommand."""

    Data: str

    @classmethod
    def response_to_model(cls, bytes_response: str) -> SingleWriteResponse:
        """parse str to model."""
        results: dict[str, Any] = {
            "Device_Address": bytes_response[:2],
            "Function_Code": FunctionCode.map_value(bytes_response[2:4]),
            "Register_Address": bytes_response[4:8],
            "Data": bytes_response[8:-4],
            "Crc16": bytes_response[-4:],
        }
        return cls(**results)


class SetupWriteResponse(BaseResponseModel):
    """Response for MultiWriteCommand."""

    Register_Count: int

    @classmethod
    def response_to_model(cls, bytes_response: str) -> SetupWriteResponse:
        """
        parse str to model.
        :param bytes_response:
        :return:
        """
        results: dict[str, Any] = {
            "Device_Address": bytes_response[:2],
            "Function_Code": FunctionCode.map_value(bytes_response[2:4]),
            "Register_Address": bytes_response[4:8],
            "Register_Count": int(bytes_response[8:-4], 16),
            "Crc16": bytes_response[-4:],
        }
        return cls(**results)


class MultiWriteResponse(BaseResponseModel):
    """Response for MultiWriteCommand."""

    Register_Count: int

    @classmethod
    def response_to_model(cls, bytes_response: str) -> MultiWriteResponse:
        """
        parse str to model.
        :param bytes_response:
        :return:
        """
        results: dict[str, Any] = {
            "Device_Address": bytes_response[:2],
            "Function_Code": FunctionCode.map_value(bytes_response[2:4]),
            "Register_Address": bytes_response[4:8],
            "Register_Count": int(bytes_response[8:-4], 16),
            "Crc16": bytes_response[-4:],
        }
        return cls(**results)
