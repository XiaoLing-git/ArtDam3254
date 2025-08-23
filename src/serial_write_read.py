import logging
import time

from src.errors import SerialReadException, SerialWriteException
from src.serial_connection import SerialConnection
from src.utils import assert_hex_code, modbus_crc16

logger = logging.getLogger(__name__)


class SerialWriteRead(SerialConnection):

    def write(self, cmd: str) -> None:
        """
        write cmd code
        :param cmd:
        :return:
        """
        assert_hex_code(cmd)
        crc16: str = modbus_crc16(cmd)
        cmd_with_crc: str = cmd.upper() + crc16
        logger.debug(f"Write: {cmd_with_crc}")
        try:
            self._ser.write(bytes.fromhex(cmd_with_crc))
        except Exception as e:
            raise SerialWriteException(f"Write Command:{cmd_with_crc} Fail {e}")

    def __read(self) -> str:
        buffer_length: int = self._ser.in_waiting
        if buffer_length == 0:
            return ""
        else:
            try:
                response: str = self._ser.read(buffer_length).hex()
            except Exception as e:
                raise SerialReadException(f"Serial Read Exception Happened {e}")
            logger.debug(f" Read: {response}")
            return response

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

    def read(self, timeout: float) -> str:
        """
        Read until get something
        :param timeout:
        :return:
        """
        start_time: float = time.time()
        while True:
            duration: float = time.time() - start_time
            if duration > timeout:
                response = None
                break
            response = self.__read()
            if len(response) > 0:
                break
        if response is None:
            raise SerialReadException(f"Serial read timeout error  timeout={timeout}")
        return response
