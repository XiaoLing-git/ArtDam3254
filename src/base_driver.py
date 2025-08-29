"""base_driver.py"""

import logging

from src.commands import BaseReadCommand, BaseWriteCommand, InputReadCommand, SingleWriteCommand, SwitchReadCommand
from src.m_type import (
    AnalogChannel,
    AnalogChannelMapAddress,
    AnalogChannelMapRangeAddress,
    AnalogInputRange,
    DigitalInputWorkMode,
    DigitalOutputMode,
    FunctionCode,
    SwitchStatus,
)
from src.models import Base_Driver_Log_Output
from src.register_address import Analog_Channel_Address, DI1_Work_Mode, DI_1_Status, DO1_Work_Mode
from src.responses import BaseReadResponse, BaseResponseModel, MultiWritResponse, SingleWriteResponse
from src.serial_write_read import SerialWriteRead
from src.utils import fill_data, register_map_value

logger = logging.getLogger(__name__)


class BaseDriver(SerialWriteRead):
    """base driver for Art device"""

    __slots__ = ("__address",)

    def __init__(self, port: str, baud_rate: int, timeout: float, device_address: str):
        """
        Base Driver init
        :param port:
        :param baud_rate:
        :param timeout:
        :param device_address:
        """
        super().__init__(port, baud_rate, timeout)

        self.__address = device_address

    def send_command(self, cmd: BaseReadCommand | BaseWriteCommand) -> None:
        """
        send model command
        :param cmd:
        :return:
        """
        if Base_Driver_Log_Output:
            logger.debug(cmd)
        self.write(cmd.CMD)

    def get_response(self, timeout: float = 2) -> BaseResponseModel:
        """
        get model response
        :param timeout:
        :return:
        """
        response: str = self.read(timeout=timeout)
        function_code = FunctionCode.map_value(response[2:4])
        if function_code is FunctionCode.SingleWrite:
            response_model = SingleWriteResponse.response_to_model(response)
        elif function_code is FunctionCode.MultiWrite:
            response_model = MultiWritResponse.response_to_model(response)
        else:
            response_model = BaseReadResponse.response_to_model(response)
        if Base_Driver_Log_Output:
            logger.debug(response_model)
        return response_model

    def get_analog_channel_value(self, channel: AnalogChannel) -> int:
        """
        get target analog channel sample value
        :param channel:
        :return:
        """
        if channel is AnalogChannel.all:
            raise ValueError("Wrong Args, Try use get_all_analog_channel_value")
        else:
            address: int = AnalogChannelMapAddress[channel]
            cmd = InputReadCommand(
                Device_Address=self.__address, Register_Address=register_map_value(address), Register_Count=1
            )
            self.send_command(cmd)
            response = self.get_response()
            data: int = int(response.Data, 16)
            return data

    def get_all_analog_channel_value(self) -> list[int]:
        """
        get all analog channel sample value
        :return:
        """
        cmd = InputReadCommand(
            Device_Address=self.__address, Register_Address=register_map_value(Analog_Channel_Address), Register_Count=4
        )
        self.send_command(cmd)
        chunk_size = 4
        response = self.get_response().Data
        return [int(response[i : i + chunk_size], 16) for i in range(0, len(response), chunk_size)]

    def get_analog_channel_range(self, channel: AnalogChannel) -> AnalogInputRange:
        """
        get analog channel range
        :param channel:
        :return:
        """
        cmd = InputReadCommand(
            Device_Address=self.__address,
            Register_Address=register_map_value(AnalogChannelMapRangeAddress[channel]),
            Register_Count=1,
        )
        self.send_command(cmd)
        response = self.get_response()
        return AnalogInputRange.map_value(response.Data)

    def set_analog_channel_range(self, channel: AnalogChannel, mode: AnalogInputRange) -> AnalogInputRange:
        """
        set and get analog_channel_range
        :param channel:
        :param mode:
        :return:
        """
        cmd = SingleWriteCommand(
            Device_Address=self.__address,
            Register_Address=register_map_value(AnalogChannelMapRangeAddress[channel]),
            Data=fill_data(mode.value),
        )
        self.send_command(cmd)
        response = self.get_response()
        return AnalogInputRange.map_value(response.Data)

    def get_digital_input_1_mode(self) -> DigitalInputWorkMode:
        """
        get digital input channel mode
        :return:
        """
        cmd = InputReadCommand(
            Device_Address=self.__address, Register_Address=register_map_value(DI1_Work_Mode), Register_Count=1
        )
        self.send_command(cmd)
        response = self.get_response()
        data: int = int(response.Data, 16)
        return DigitalInputWorkMode.map_value(data)

    def set_digital_input_1_work_mode(self, mode: DigitalInputWorkMode) -> DigitalInputWorkMode:
        """
        set and get digital input channel work mode
        :return:
        """
        hex_char: str = hex(mode.value).replace("0x", "")
        cmd = SingleWriteCommand(
            Device_Address=self.__address, Register_Address=register_map_value(DI1_Work_Mode), Data=fill_data(hex_char)
        )
        self.send_command(cmd)
        response = self.get_response()
        data: int = int(response.Data, 16)
        return DigitalInputWorkMode.map_value(data)

    def get_digital_output_1_mode(self) -> DigitalOutputMode:
        """
        get digital output channel mode
        :return:
        """
        cmd = InputReadCommand(
            Device_Address=self.__address, Register_Address=register_map_value(DO1_Work_Mode), Register_Count=1
        )
        self.send_command(cmd)
        response = self.get_response()
        data: int = int(response.Data, 16)
        return DigitalOutputMode.map_value(data)

    def set_digital_output_1_mode(self, mode: DigitalOutputMode) -> DigitalOutputMode:
        """
        set and get digital output channel mode
        :return:
        """
        hex_char: str = hex(mode.value).replace("0x", "")
        cmd = SingleWriteCommand(
            Device_Address=self.__address, Register_Address=register_map_value(DO1_Work_Mode), Data=fill_data(hex_char)
        )
        self.send_command(cmd)
        response = self.get_response()
        data: int = int(response.Data, 16)
        return DigitalOutputMode.map_value(data)

    def get_digital_input_1_status(self) -> SwitchStatus:
        """
        get digital input 1 status
        :return:
        """
        cmd = SwitchReadCommand(
            Device_Address=self.__address,
            Register_Address=DI_1_Status,
            Register_Count=1,
        )
        self.send_command(cmd)
        response = self.get_response()
        return SwitchStatus.map_value(response.Data)
