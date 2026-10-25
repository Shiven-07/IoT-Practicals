"""Local lab demonstration; no authentication. Do not expose to the internet."""
from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
LIGHT, FAN = 17, 27  # BCM pin numbers
ON, OFF = GPIO.HIGH, GPIO.LOW  # For an active-HIGH relay board.

@app.route("/")
def home():
    return """<!doctype html><html lang="en"><title>IoT Home Automation</title>
    <h1>IoT Home Automation</h1>
    <h2>Light</h2><a href="/light/on">ON</a> | <a href="/light/off">OFF</a>
    <h2>Fan</h2><a href="/fan/on">ON</a> | <a href="/fan/off">OFF</a>
    </html>"""

@app.route("/light/on")
def light_on():
    GPIO.output(LIGHT, ON)
    return 'Light ON. <a href="/">Back</a>'

@app.route("/light/off")
def light_off():
    GPIO.output(LIGHT, OFF)
    return 'Light OFF. <a href="/">Back</a>'

@app.route("/fan/on")
def fan_on():
    GPIO.output(FAN, ON)
    return 'Fan ON. <a href="/">Back</a>'

@app.route("/fan/off")
def fan_off():
    GPIO.output(FAN, OFF)
    return 'Fan OFF. <a href="/">Back</a>'

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup((LIGHT, FAN), GPIO.OUT, initial=OFF)
    try:
        app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
    finally:
        GPIO.output((LIGHT, FAN), OFF)
        GPIO.cleanup()

if __name__ == "__main__":
    main()
