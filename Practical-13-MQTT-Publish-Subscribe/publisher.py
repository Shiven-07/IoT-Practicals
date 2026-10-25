import paho.mqtt.client as mqtt

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect("localhost", 1883, 60)
    client.loop_start()
    try:
        while True:
            command = input("ON / OFF / quit: ").strip().upper()
            if command == "QUIT":
                break
            if command not in ("ON", "OFF"):
                continue
            delivery = client.publish("iot/led", command, qos=1)
            delivery.wait_for_publish(timeout=5)
            print("Published:" if delivery.is_published() else "Delivery timed out:", command)
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()
        client.loop_stop()

if __name__ == "__main__":
    main()
