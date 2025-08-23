import logging

from .errors import DeviceAddressException, HexCodeException, ModBusCrc16Exception, RegisterAddressException

logger = logging.getLogger(__name__)


def assert_hex_code(target: str) -> None:
    """
    assert target is hex code
    :param target:
    :return:
    """
    if len(target) == 0:
        return
    for c in target:
        if c.upper() not in "0123456789ABCDEF":
            raise HexCodeException(f"char {c} can't not hex()")
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
    logger.debug(f"Crc16 Target: {target} Result: {result}")
    return result.upper()
