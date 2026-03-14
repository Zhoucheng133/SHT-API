# SHT Viz

Also available in English. Click [HERE](/documents/en.md) to view the English version of the README

## 简介

![License](https://img.shields.io/badge/License-MIT-dark_green)

适用于树莓派开发板的SHT传感器可视化系统，使用Docker进行部署

前端页面的仓库[在这里](https://github.com/Zhoucheng133/SHT-Viz-Web)

## 截图

<img src="demo/desktop.png" height=500 />
<img src="demo/mobile.png" height=500 />


## 使用Docker部署

> [!NOTE]
> 你需要修改下面命令中带有尖括号的内容

```bash
sudo docker run -d \
--restart always \
--name sht \
-p <主机端口>:8080 \
-v <主机上存储数据库的位置*>:/app/db \
--device /dev/i2c-1 \
zhouc1230/sht:latest
```

*任意，保证存在并且可以读写的目录即可

## 更新

```bash
# 拉取最新镜像
docker pull zhouc1230/sht:latest
# 停止旧容器
docker stop sht
# 删除旧容器
docker rm sht
# 启动新容器
sudo docker run -d \
--restart always \
--name sht \
-p <主机端口>:8080 \
-v <主机上存储数据库的位置*>:/app/db \
--device /dev/i2c-1 \
zhouc1230/sht:latest
```

## API

![GET](https://img.shields.io/badge//get-GET-dark_green)  
获取当前温度和湿度数据

![GET](https://img.shields.io/badge//get/day-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期的所有温湿度数据

![GET](https://img.shields.io/badge//get/max-GET-dark_green)  
获取最高气温的数据

![GET](https://img.shields.io/badge/get/min-GET-dark_green)  
获取最低气温的数据

![GET](https://img.shields.io/badge//get/maxByDay-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期高气温的数据

![GET](https://img.shields.io/badge//get/minByDay-GET-dark_green)  
?`year`&`month`&`day`  
获取指定日期低气温的数据

### 响应

```json
{
    "timestamp": "2025-01-01 00:00:00",
    "temperature": 10,
    "humidity": 60
}
```