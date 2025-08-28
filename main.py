"""Main function entry, mainly used for debugging."""

from pprint import pprint

from src.commands import FunctionCode, InputReadCommand, StateReadCommand, SingleWriteCommand, MultiWriteCommand
from src.serial_write_read import SerialWriteRead
from src.utils import assert_function_code, modbus_crc16, convert_register_length_to_hex

import logging

logging.basicConfig(
    level=logging.DEBUG,  # 核心：设置最低日志级别为DEBUG
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S'  # 时间格式
)

if __name__ == "__main__":


    swr = SerialWriteRead(port="/dev/ttyUSB0",baud_rate=9600,timeout=5)
    swr.connect()

    ic = InputReadCommand(Device_Address="01",
                          Register_Address="0000",
                          Register_Count=2)
    swr.write(str(ic))
    res = swr.read(timeout=5)
    print(res)

    ic = StateReadCommand(Device_Address="01",
                          Register_Address="0080",
                          Register_Count=7)
    swr.write(str(ic))
    res = swr.read(timeout=5)
    print(res)

    ic = SingleWriteCommand(Device_Address="01",
                          Register_Address="0084",
                          Data="0002")
    swr.write(str(ic))
    res = swr.read(timeout=5)
    print(res)

    ic = MultiWriteCommand(Device_Address="01",
                            Register_Address="0084",
                            Data="000200030000")
    swr.write(str(ic))
    res = swr.read(timeout=5)
    print(res)




    swr.disconnect()