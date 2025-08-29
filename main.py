"""Main function entry, mainly used for debugging."""
from src.base_driver import BaseDriver
from src.m_type import AnalogChannel, DigitalInputMode
from src.models import Serial_Write_Read_Log_Output,Modbus_Crc16_Log_Output


from src.commands import FunctionCode, InputReadCommand, StateReadCommand, SingleWriteCommand, MultiWriteCommand
from src.responses import BaseResponseModel, BaseReadResponse, SingleWriteResponse, MultiWritResponse
from src.serial_write_read import SerialWriteRead
from src.utils import assert_function_code, modbus_crc16, convert_register_length_to_hex

import logging

logging.basicConfig(
    level=logging.DEBUG,  # 核心：设置最低日志级别为DEBUG
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S'  # 时间格式
)

if __name__ == "__main__":

    swr = BaseDriver(port="/dev/ttyUSB0",baud_rate=9600,timeout=5,device_address="01")
    swr.connect()

    # res = swr.get_analog_channel_value(AnalogChannel.ch1)
    # print(res)
    #
    # res = swr.get_analog_channel_value(AnalogChannel.ch2)
    # print(res)
    #
    # res = swr.get_analog_channel_value(AnalogChannel.ch3)
    # print(res)
    #
    # res = swr.get_analog_channel_value(AnalogChannel.ch4)
    # print(res)
    #
    # res = swr.get_all_analog_channel_value()
    # print(res)

    res = swr.get_digital_input_1_mode()
    print(res)
    res = swr.get_digital_output_1_mode()
    print(res)




    swr.disconnect()