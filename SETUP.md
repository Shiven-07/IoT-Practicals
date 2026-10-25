# Setup guide

## Raspberry Pi environment

Use the lab's Raspberry Pi 4 and Raspberry Pi OS setup. Run each practical separately from its own folder. Python 3.9 or newer is needed by the supplied study code. Hardware libraries generally cannot execute on this Windows computer.

On the Pi, create a virtual environment after installing the OS support packages needed by that practical:

~~~bash
sudo apt update
sudo apt install python3-venv python3-pip
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
~~~

Run the requirements command only in folders that contain requirements.txt. For Flask folders, run python app.py. Practical 13 has two programs. Practical 3 needs the lab's tm1637.py driver. This guide does not repeat the source's global break-system-packages setting or uninstall/reinstall workaround.

Picamera2: install the OS python3-picamera2 package. Motion detection also needs python3-opencv. Use the virtual environment with system-site-packages so these OS packages remain visible.

## Interfaces and numbering

Enable the interface needed by the practical in raspi-config:
- I2C: LCD and ADS1115.
- SPI: MFRC522 RFID.
- UART: GPS and direct-serial fingerprint sensors. Disable the serial login shell when using the port for a sensor.

Do not mix BCM GPIO numbers with physical BOARD pin numbers. Each script identifies its convention. The combined RFID scripts use BOARD numbering: physical 12 = BCM18, physical 11 = BCM17, physical 13 = BCM27. They retain RFID reset at physical 22 = BCM25.

For I2C addressing, install i2c-tools and inspect i2cdetect -y 1. LCD examples default to 0x27; change it to the detected address.

## Electrical details to verify

The source mixes 5 V supply pins with GPIO signal connections. Raspberry Pi GPIO uses 3.3 V logic and is not 5 V tolerant. Confirm your exact module and use suitable level shifting where 5 V pull-ups or outputs would reach the Pi. Check the ADS1115 supply and analog-input limits before connecting the MQ2 output. Power the MFRC522 from 3.3 V. [Raspberry Pi GPIO documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio)

Use resistor-limited LEDs and low-voltage demonstration loads. Do not wire mains electricity for these exercises. The relay examples explicitly distinguish active-HIGH and active-LOW inputs; check the board before attaching a load.

## Telegram

Create your own bot through BotFather and use your own numeric chat ID. Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in the Pi shell environment. Do not commit real values. .env.example contains placeholders only and is not loaded automatically. The code uses the PDF's legacy telepot dependency; online operation has not been verified.

## MQTT

Install the local broker:

~~~bash
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto
~~~

Run subscriber.py and publisher.py in separate terminals on that Pi, with the same virtual environment activated. Paho 2.x is specified because the programs use CallbackAPIVersion.VERSION2. [Paho documentation](https://eclipse.dev/paho/clients/python/docs/)

## Fingerprint and RFID exercises

Enroll test fingerprints on your own sensor with Practical 8. For direct UART enrollment set FINGERPRINT_PORT=/dev/serial0; its default is /dev/ttyUSB0 for a compatible USB-to-UART adapter. Use Practical 7 to read your tag UID. Supply your own allowlist values in Practicals 15 and 19.

Practical 15 requires both a configured card and an enrolled fingerprint. Practical 19 accepts either method. The examples do not map a specific card to a specific person's finger. Keep generated access_log.csv and captured images local; they are ignored by Git.

## Windows IoT Core

Practical 20 is a legacy UWP exercise requiring a compatible board, image, Visual Studio installation and Windows SDK. A Raspberry Pi 4 setup used for the Python practicals should not be assumed compatible. The two page files need a generated UWP project; they are not a standalone executable. Confirm the lab's supported image before flashing any card.

## GitHub

The repository is an organized reference and code collection. Download with Code > Download ZIP or clone it with GitHub Desktop. The PDFs preserve existing diagrams and screenshots; empty results and Input IMAGE placeholders in the book remain empty.
