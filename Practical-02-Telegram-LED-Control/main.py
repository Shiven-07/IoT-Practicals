"""Python 3 adaptation using the PDF's legacy telepot library."""
import os
from threading import Event
import telepot
import RPi.GPIO as GPIO

LED = 11  # BOARD pin 11 = BCM17
stop = Event()

def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    allowed_chat = int(os.environ["TELEGRAM_CHAT_ID"])
    bot = telepot.Bot(token)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

    def handle(msg):
        if stop.is_set() or msg.get("chat", {}).get("id") != allowed_chat:
            return
        command = msg.get("text", "").strip().lower()
        if command == "on":
            GPIO.output(LED, GPIO.HIGH)
            bot.sendMessage(allowed_chat, "LED on")
        elif command == "off":
            GPIO.output(LED, GPIO.LOW)
            bot.sendMessage(allowed_chat, "LED off")
        elif command == "stop":
            stop.set()

    try:
        bot.message_loop(handle)
        print("Listening for on, off and stop in the configured chat.")
        stop.wait()
    except KeyboardInterrupt:
        stop.set()
    finally:
        stop.set()
        GPIO.output(LED, GPIO.LOW)
        GPIO.cleanup()

if __name__ == "__main__":
    main()
