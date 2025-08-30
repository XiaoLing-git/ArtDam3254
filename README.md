# RigolDp700
 Python Support for [DAM-3254](http://www.art-control.com/productShow_2491.html) Series power supplies.

## Company
http://www.art-control.com/

## Notes:

Before you start it, please make sure you have installed the following tools

- make == GNU Make 4.4.1
- poetry == 1.8.0
- python == 3.10.*

## Commands

### Build Wheel

```bash
make build
```

### Install Local

```bash
make install
```

### Enter Venv 

```bash
make shell
```

### Clean

```bash
make clean
```

### Commit To Github

```bash
make commit msg="comments"
make push msg="comments"
```

### Local check code

```bash
make check
```


### Example
```python
swr = BaseDriver(port="/dev/ttyUSB0",baud_rate=9600,timeout=5,device_address="01")
swr.connect()

res = swr.get_analog_channel_value(AnalogChannel.ch1)
print(res)

res = swr.get_analog_channel_value(AnalogChannel.ch2)
print(res)

res = swr.get_analog_channel_value(AnalogChannel.ch3)
print(res)

res = swr.get_analog_channel_value(AnalogChannel.ch4)
print(res)

res = swr.get_all_analog_channel_value()
print(res)

res = swr.get_digital_input_1_work_mode()
print(res)

res = swr.get_analog_channel_range(AnalogChannel.ch1)
print(res)

res = swr.get_digital_input_1_status()
print(res)

res = swr.set_digital_output_1_status(SwitchStatus.Off,DigitalOutputMode.Engage)

swr.disconnect()
```

