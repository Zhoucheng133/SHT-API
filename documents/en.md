# SHT Viz

## Introduction

![License](https://img.shields.io/badge/License-MIT-dark_green)

SHT sensor visualization system for Raspberry Pi. Deployed with Docker.

Front-End Repo is [HERE](https://github.com/Zhoucheng133/SHT-Viz-Web)

## Screenshots

<img src="../demo/desktop.png" height=500 />
<img src="../demo/mobile.png" height=500 />

## Deploy with Docker

> [!NOTE]
> You need to modify the content in the angle brackets

```bash
sudo docker run -d \
--restart always \
--name sht \
-p <Host Port>:8080 \
-v <Location of database on host*>:/app/db \
--device /dev/i2c-1 \
zhouc1230/sht:latest
```

*Any directory that exists and can be read and written is acceptable.

## Update

```bash
# Pull latest image
docker pull zhouc1230/sht:latest
# Stop old container
docker stop sht
# Delete old container
docker rm sht
# Start new container
sudo docker run -d \
--restart always \
--name sht \
-p <Host Port>:8080 \
-v <Location of database on host*>:/app/db \
--device /dev/i2c-1 \
zhouc1230/sht:latest
```

## API

![GET](https://img.shields.io/badge//get-GET-dark_green)  
Get current temperature and humidity

![GET](https://img.shields.io/badge//get/day-GET-dark_green)  
?`year`&`month`&`day`  
Get all temperature and humidity data for a specified date

![GET](https://img.shields.io/badge//max-GET-dark_green)  
Get the highest temperature data

![GET](https://img.shields.io/badge//min-GET-dark_green)  
Get the lowest temperature data

![GET](https://img.shields.io/badge//maxByDay-GET-dark_green)  
?`year`&`month`&`day`  
Get the highest temperature data for a specified date

![GET](https://img.shields.io/badge//minByDay-GET-dark_green)  
?`year`&`month`&`day`  
Get the lowest temperature data for a specified date

### Response

```json
{
    "timestamp": "2025-01-01 00:00:00",
    "temperature": 10,
    "humidity": 60
}
```