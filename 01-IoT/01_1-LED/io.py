# Import library and create instance of REST client.
from gpiozero import LED
from Adafruit_IO import Client
import time
aio = Client('YOUR_USERNAME', 'YOUR_KEY')

led = LED(17)
# Send the value 100 to a feed called 'Foo'.

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
'''data = aio.feeds('value')
while True:
    aio.send_data(data.key, 10)
    time.sleep(3)
'''

'''while True:
    data = aio.receive('led')
    if data.value == "OFF":
        led.off()
        print('Received value: {0}'.format(data.value))
    else:
        led.on()
        print('Received value: {0}'.format(data.value))
'''
feeds = aio.feeds()
print(feeds)
