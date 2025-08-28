"""SerialWriteRead."""

import logging
import time

from src.errors import SerialReadException, SerialWriteException
from src.models import Serial_Write_Read_Log_Clean_Output, Serial_Write_Read_Log_Output
from src.serial_connection import SerialConnection
from src.utils import assert_hex_code, modbus_crc16

logger = logging.getLogger(__name__)


class SerialWriteRead(SerialConnection):
    """
    SerialWriteRead
    """

    def write(self, cmd: str) -> None:
        """
        write cmd code
        :param cmd:
        :return:
        """
        assert_hex_code(cmd)
        if Serial_Write_Read_Log_Output:
            logger.debug(f"Write: {cmd}")
        try:
            self._ser.write(bytes.fromhex(cmd))
        except Exception as e:
            raise SerialWriteException(f"Write Command:{cmd} Fail {e}")

    def __read(self) -> str:
        buffer_length: int = self._ser.in_waiting
        if buffer_length == 0:
            return ""
        else:
            try:
                response: str = self._ser.read(buffer_length).hex()
            except Exception as e:
                raise SerialReadException(f"Serial Read Exception Happened {e}")
            return response.upper()

    def read_size(self, size: int, timeout: float) -> str:
        """
        Read a certain amount of bytes
        :param size:
        :param timeout:
        :return:
        """
        start_time: float = time.time()
        response: str = ""
        while True:
            duration: float = time.time() - start_time
            if duration > timeout:
                break
            response = response + self.__read()
            if len(response) == size:
                break
        current_size = len(response)
        if current_size != size:
            raise SerialReadException(f"Serial read timeout error, Current Size = {current_size} Timeout={timeout}")
        logger.debug(f" ReadSize: Size = {current_size}, Response = {response}")
        return response

    def read(self, timeout: float = 2) -> str:
        """
        Read until get something
        :param timeout:
        :return:
        """
        time.sleep(0.1)
        start_time: float = time.time()
        response: str = ""
        while True:
            duration: float = time.time() - start_time
            _length: int = len(response)
            if duration > timeout:
                raise SerialReadException(f"Serial read timeout, " f"Response = {response}, " f"Timeout={timeout}")
            response = response + self.__read()
            if _length < 4:
                continue
            content: str = response[:-4]
            crc16: str = response[-4:]
            if modbus_crc16(content) == crc16:
                break
        if Serial_Write_Read_Log_Output:
            logger.debug(f" Read: {response}")
        if Serial_Write_Read_Log_Clean_Output:
            logger.debug("-" * 100)
        return response
