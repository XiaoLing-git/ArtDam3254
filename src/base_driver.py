"""base_driver.py"""

import logging

from src.commands import BaseReadCommand, BaseWriteCommand
from src.m_type import FunctionCode
from src.models import Base_Driver_Log_Output
from src.responses import BaseReadResponse, BaseResponseModel, MultiWritResponse, SingleWriteResponse
from src.serial_write_read import SerialWriteRead

logger = logging.getLogger(__name__)


class BaseDriver(SerialWriteRead):
    """base driver for Art device"""

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
