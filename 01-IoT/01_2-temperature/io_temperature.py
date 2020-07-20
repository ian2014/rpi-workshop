from Adafruit_IO import Client, Feed
import json

import time
import board
import adafruit_dht


ADAFRUIT_IO_KEY = "YOUR_KEY"
ADAFRUIT_IO_USERNAME = "YOUR_USERNAME"

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
temperature = aio.feeds("temperature")
text = aio.feeds("text")


dhtDevice = adafruit_dht.DHT11(board.D4)
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        data = "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity)
        aio.send_data(temperature.key, data)
        aio.send_data(text.key, data)
        print(data)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

    time.sleep(2.0)

