import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

@app.route("/")
def main():
  return render_template('main.html')

@app.route("/led/on")
def led_on():
    GPIO.output(17, GPIO.HIGH)
    return render_template('main.html')

@app.route("/led/off")
def led_off():
    GPIO.output(17, GPIO.LOW)
    return render_template('main.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)