# SHT API

针对树莓派（开发板）的SHT温度/湿度API和数据存储

> [!WARNING]
> 这是一个仍在测试中的项目

## API

![GET](https://img.shields.io/badge//get-GET-dark_green)  
获取当前温度和湿度数据

![GET](https://img.shields.io/badge//get/day-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期的所有温湿度数据

![GET](https://img.shields.io/badge//max-GET-dark_green)  
获取最高气温的数据

![GET](https://img.shields.io/badge//min-GET-dark_green)  
获取最低气温的数据

![GET](https://img.shields.io/badge//maxByDay-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期高气温的数据

![GET](https://img.shields.io/badge//minByDay-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期低气温的数据

## 响应

```json
{
    "timestamp": "2025-01-01 00:00:00",
    "temperature": 10,
    "humidity": 60
}
```