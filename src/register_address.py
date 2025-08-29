"""register_address.py"""

Analog_Channel_Address: int = 40001
# 第 0 路模拟量采集值
Analog_Channel_1_Address: int = 40001
# 第 1 路模拟量采集值
Analog_Channel_2_Address: int = 40002
# 第 2 路模拟量采集值
Analog_Channel_3_Address: int = 40003
# 第 3 路模拟量采集值
Analog_Channel_4_Address: int = 40004

# 第 0 路模拟量输入量程
Analog_Channel_1_Range: int = 40201
# 第 1 路模拟量输入量程
Analog_Channel_2_Range: int = 40202
# 第 2 路模拟量输入量程
Analog_Channel_3_Range: int = 40203
# 第 4 路模拟量输入量程
Analog_Channel_4_Range: int = 40204
# DI0 计数值/频率值低 16 位
DI_1_Counter_Freq_Low: int = 40289
# DI0 计数值/频率值高 16 位
DI_1_Counter_Freq_High: int = 40290
# 主动上传使能
Upload_Enable: int = 40578
# DO0 工作模式
DO1_Work_Mode: int = 41001
# DI0 工作模式
DI1_Work_Mode: int = 41649
# DO0 脉冲输出高电平宽度高 16 位
DO_1_Pulse_Output_High_Level_Width_High: int = 41033
# DO0 脉冲输出高电平宽度低 16 位
DO_1_Pulse_Output_High_Level_Width_Low: int = 41034

# DO0 脉冲输出低电平宽度高 16 位
DO_1_Pulse_Output_Low_Level_Width_High: int = 41065
# DO0 脉冲输出低电平宽度低 16 位
DO_1_Pulse_Output_Low_Level_Width_Low: int = 41066
# DO0 脉冲输出个数高 16 位
DO_1_Pulse_Output_Count_High: int = 41129
# DO0 脉冲输出个数低 16 位
DO_1_Pulse_Output_Count_Low: int = 41130
# DO0 低到高输出延迟时间高 16 位
DO_1_Output_Low_to_High_Delay_High: int = 41161
# DO0 低到高输出延迟时间低 16 位
DO_1_Output_Low_to_High_Delay_Low: int = 41162
# DO0 低到高输出延迟时间高 16 位
DO_1_Output_High_to_Low_Delay_High: int = 41193
# DO0 低到高输出延迟时间低 16 位
DO_1_Output_High_to_Low_Delay_Low: int = 41194
# DO0 脉冲输出增加个数高 16 位
DO_1_Pulse_Output_Increase_Number_High: int = 41193
# DO0 脉冲输出增加个数低 16 位
DO_1_Pulse_Output_Increase_Number_Low: int = 41194

# D00 输出状态
DO_1_Output_Status_Normal: int = 1
# DO0 上电输出状态
DO_1_Output_Status_Pull: int = 33
# DI0 锁存状态
DI_1_Latch_status: int = 633
# DI0 过滤使能
DI_1_Filter_enable: int = 665
# DI0 反向
DI_1_Reverse_Flag: int = 681
# DI0 计数器启停
DI_1_Counter_Switch: int = 697
# DI0 过滤使能
DI_1_OverFlow_Flag: int = 729


Device_Model: int = 40129
Device_Model_Suffix: int = 40130
Device_Protocol: int = 40131
Device_Version: int = 40132
Device_Baudrate: int = 40134
Device_Parity: int = 40135
