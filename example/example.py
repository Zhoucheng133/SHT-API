import smbus
import time

bus = smbus.SMBus(1)
SHT30_ADDR = 0x44

def read_sht30():
    # 发送启动测量命令
    bus.write_i2c_block_data(SHT30_ADDR, 0x2C, [0x06])
    time.sleep(0.05)
    
    data = bus.read_i2c_block_data(SHT30_ADDR, 0, 6)
    if len(data) != 6:
        return None, None
    
    temp_raw = (data[0] << 8) | data[1]
    temperature = -45 + (175 * temp_raw) / 65535.0
    
    humi_raw = (data[3] << 8) | data[4]
    humidity = 100 * humi_raw / 65535.0
    
    return round(temperature, 2), round(humidity, 2)

temp, humi = read_sht30()
if temp is not None and humi is not None:
    print(f"温度：{temp} °C，湿度：{humi} %")
else:
    print("读取传感器失败")
