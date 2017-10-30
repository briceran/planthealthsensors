from sense_hat import SenseHat
from time import strftime

sense = SenseHat()
sense.clear()


# main loop
while True:
	sensor_data = []
	timestamp = strftime("%Y-%m-%d %H:%M:%S")
        sensor_data.insert(0, timestamp)
	pressure = sense.get_pressure()
	temp = sense.get_temperature()
        humidity = sense.get_humidity()
        sensor_data.insert(0, pressure)
        sensor_data.insert(0, temp)
        sensor_data.insert(0, humidity)
        print sensor_data

        
	
