"""Utils."""

import logging
import time

from ..errors import (
    DeviceAddressException,
    HexCodeException,
    ModBusCrc16Exception,
    RegisterAddressException,
    SingleDataFormatError,
)
from ..models.common import Modbus_Crc16_Log_Output

logger = logging.getLogger(__name__)


def assert_hex_code(target: str) -> None:
    """
    assert target is hex code,
    :param target:
    :return:
    """
    if len(target) == 0:
        return
    for c in target:
        if c.upper() not in "0123456789ABCDEF":
            raise HexCodeException(f"char {c} can't not hex()")
    return


def assert_single_data(target: str) -> None:
    """
    assert single data format,
    :param target:
    :return:
    """
    assert_hex_code(target)

    if len(target) != 4:
        raise SingleDataFormatError(f"Single Data Str's Length should Be 4, Now = {len(target)}")
    return


def assert_1_byte_data(target: str) -> None:
    """
    assert single data format,
    :param target:
    :return:
    """
    assert_hex_code(target)

    if len(target) != 2:
        raise SingleDataFormatError(f"Single Data Str's Length should Be 2, Now = {len(target)}")
    return


def assert_device_address(target: str) -> None:
    """
    assert device address format
    :param target:
    :return:
    """
    if len(target) != 2:
        raise DeviceAddressException("Length Of Device Address Not Equal 2")
    try:
        assert_hex_code(target)
    except Exception as e:
        raise DeviceAddressException(f"{e}")
    return


def assert_register_address(target: str) -> None:
    """
    assert register address format
    :param target:
    :return:
    """
    if len(target) != 4:
        raise RegisterAddressException("Length Of Device Address Not Equal 4")
    try:
        assert_hex_code(target)
    except Exception as e:
        raise RegisterAddressException(f"{e}")
    return


def modbus_crc16(target: str) -> str:
    """Calculate modbus crc code."""
    if len(target) == 0:
        raise ModBusCrc16Exception("length target data is 0")

    try:
        data: bytes = bytes.fromhex(target)
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        result: str = crc.to_bytes(2, byteorder="little").hex()
    except Exception as e:
        raise ModBusCrc16Exception(f"An exception occurred during calculation: {e}")
    if Modbus_Crc16_Log_Output:
        logger.debug(f"Crc16 Target: {target.upper()} Result: {result.upper()}")
    return result.upper()


def convert_register_length_to_hex(_length: int) -> str:
    """
    Convert register length to recognizable hexadecimal characters
    :param _length:
    :return:
    """
    if _length < 0 or _length > 65535:
        msg: str = f"Length of Register musy be  0 < Length  < 65536, current = {_length}"
        logger.error(msg)
        raise ValueError(msg)
    hex_char: str = hex(_length).replace("0x", "")
    start_time: float = time.time()
    while len(hex_char) != 4:
        if time.time() - start_time > 1:
            break
        hex_char = "0" + hex_char
    return hex_char.upper()


def register_map_value(address: int) -> str:
    """
    register map value
    :param address:
    :return:
    """
    return convert_register_length_to_hex(address - 40001)


def fill_data(target: str, _length: int = 4) -> str:
    """
    fill data
    :param target:
    :param _length:
    :return:
    """
    if len(target) > _length:
        raise ValueError(f"Current length of {target} great than {_length}")
    start_time: float = time.time()
    while len(target) != _length:
        if time.time() - start_time > 1:
            break
        target = "0" + target
    return target
