from gpiozero import LED
from flask import Flask, render_template

app = Flask(__name__)

led = LED(17)

@app.route("/")
def main():
  return render_template('main.html')

@app.route("/led/on")
def led_on():
    led.on()
    return render_template('main.html')

@app.route("/led/off")
def led_off():
    led.off()
    return render_template('main.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
