import logging

from .errors import HexCodeException, ModBusCrc16Exception

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
    return result
