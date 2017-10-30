from sense_hat import sense_hat
from time import strftime

sense = SenseHat()
sense.clear()


# main loop
while True:
	sensor_data = []
	timestamp = strftime("%Y-%m-%d %H:%M:%S")
	print timestamp
	sensor_data.insert(0, timestamp)
	print sensor_data
    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    sensor_data.insert(0, pressure)
    sensor_data.insert(0, temp)
    sensor_data.insert(0, humidity)
	time.sleep(10)
