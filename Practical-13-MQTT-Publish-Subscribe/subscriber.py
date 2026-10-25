import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

LED = 18  # BCM
TOPIC = "iot/led"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected")
        client.subscribe(TOPIC)
    else:
        print("Connection refused:", reason_code)

def on_message(client, userdata, message):
    command = message.payload.decode("utf-8", errors="replace").strip().upper()
    if command == "ON":
        GPIO.output(LED, GPIO.HIGH)
    elif command == "OFF":
        GPIO.output(LED, GPIO.LOW)
    else:
        return
    print("LED", command)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect("localhost", 1883, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()
        GPIO.output(LED, GPIO.LOW)
        GPIO.cleanup()

if __name__ == "__main__":
    main()
