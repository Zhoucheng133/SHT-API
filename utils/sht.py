from datetime import datetime, timedelta
import sqlite3
import threading
import time
import smbus

bus = smbus.SMBus(1)
SHT30_ADDR = 0x44

class ShtSensor:
    def __init__(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS temperature_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL
        )
        ''')
        conn.commit()
        
        threading.Thread(target=self.loop, daemon=True).start()
    
    def loop(self):
        while True:
            now = datetime.now()
            next_minute = (now.minute // 10 + 1) * 10
            if next_minute >= 60:
                next_time = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
            else:
                next_time = now.replace(minute=next_minute, second=0, microsecond=0)
            sleep_seconds = (next_time - now).total_seconds()
            print(f"等待 {sleep_seconds:.2f} 秒执行下一次数据收集...")
            time.sleep(sleep_seconds)
            self.mainLoop()

    def mainLoop(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        sensorData = self.getSensorData()
        now = datetime.now().replace(second=0, microsecond=0)
        c.execute(
            "INSERT INTO temperature_log (timestamp, temperature, humidity) VALUES (?, ?, ?)",
            (now, sensorData["temperature"], sensorData["humidity"])
        )
        one_year_ago = now - timedelta(days=365)
        c.execute(
            "DELETE FROM temperature_log WHERE timestamp < ?",
            (one_year_ago,)
        )
        conn.commit()
        conn.close()

    def read_sht30(self):
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

    def getSensorData(self):
        temp, humi = self.read_sht30()
        return {
            "temperature": temp,
            "humidity": humi,
        }

    def getDataByDay(self, day: datetime):
        conn = sqlite3.connect("data.db")
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        day_str = day.strftime("%Y-%m-%d")
        c.execute("""
            SELECT timestamp, temperature, humidity 
            FROM temperature_log 
            WHERE DATE(timestamp) = ?
            ORDER BY timestamp ASC
        """, (day_str,))
        rows = c.fetchall()
        conn.close()
        result = [dict(row) for row in rows]
        return result

    def getMaxTemp(self):
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute("""
            SELECT timestamp, temperature, humidity
            FROM temperature_log
            ORDER BY temperature DESC
            LIMIT 1
        """)
        
        row = c.fetchone()
        conn.close()
        
        if row:
            return {"timestamp": row[0], "temperature": row[1], "humidity": row[2]}
        return None

    def getMinTemp(self):
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute("""
            SELECT timestamp, temperature, humidity
            FROM temperature_log
            ORDER BY temperature ASC
            LIMIT 1
        """)
        
        row = c.fetchone()
        conn.close()
        
        if row:
            return {"timestamp": row[0], "temperature": row[1], "humidity": row[2]}
        return None
    
    def getMaxByDay(self, timestamp: datetime):
        day_str = timestamp.strftime("%Y-%m-%d")
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute("""
            SELECT timestamp, temperature, humidity
            FROM temperature_log
            WHERE DATE(timestamp) = ?
            ORDER BY temperature DESC
            LIMIT 1
        """, (day_str,))
        row = c.fetchone()
        conn.close()
        if row:
            return {"timestamp": row[0], "temperature": row[1], "humidity": row[2]}
        return None
    
    def getMinByDay(self, timestamp: datetime):
        day_str = timestamp.strftime("%Y-%m-%d")
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        c.execute("""
            SELECT timestamp, temperature, humidity
            FROM temperature_log
            WHERE DATE(timestamp) = ?
            ORDER BY temperature ASC
            LIMIT 1
        """, (day_str,))
        row = c.fetchone()
        conn.close()
        if row:
            return {"timestamp": row[0], "temperature": row[1], "humidity": row[2]}
        return None



if __name__=="__main__":
    sht=ShtSensor()