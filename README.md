# SHT API

针对树莓派（开发板）的SHT温度/湿度API和数据存储  
SHT temperature & humidity API and data storage for Raspberry Pi (NOT Pico)

## API

![GET](https://img.shields.io/badge//get-GET-dark_green)  
获取当前温度和湿度数据  
Get current temperature and humidity

![GET](https://img.shields.io/badge//get/day-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期的所有温湿度数据  
Get all temperature and humidity data for a specified date

![GET](https://img.shields.io/badge//max-GET-dark_green)  
获取最高气温的数据  
Get the highest temperature data

![GET](https://img.shields.io/badge//min-GET-dark_green)  
获取最低气温的数据  
Get the lowest temperature data

![GET](https://img.shields.io/badge//maxByDay-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期高气温的数据
Get the highest temperature data for a specified date

![GET](https://img.shields.io/badge//minByDay-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期低气温的数据  
Get the lowest temperature data for a specified date

## 响应 | Response

```json
{
    "timestamp": "2025-01-01 00:00:00",
    "temperature": 10,
    "humidity": 60
}
```