"""Main function entry, mainly used for debugging."""

from pprint import pprint

from src.commands import FunctionCode
from src.serial_write_read import SerialWriteRead
from src.utils import assert_function_code, modbus_crc16

if __name__ == "__main__":
    swr = SerialWriteRead(port="/dev/ttyUSB0",baud_rate=9600,timeout=5)
    swr.write("010300800007")
    res = swr.read(timeout=5)
    print(res)
