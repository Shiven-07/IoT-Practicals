# IoT Practicals - Raspberry Pi & Python

🚀 Made by **Shiven Dubey** | **TYBSc IT - University of Mumbai** 🎓

A collection of **IoT, Raspberry Pi, Python, MQTT, Flask & Node-RED** practicals organized to help my friends and fellow IT students learn, code, debug, and grow together! 💻🔥

**20 practicals**, separated into folders so you can open the program you need without searching through the full book.

[Complete original practical book](IoT-Practical-Book.pdf) · [Setup guide](SETUP.md) · [Corrections and source notes](SOURCE-NOTES.md) · [Validation](VALIDATION.md)

## Practical index

| No. | Practical | Editable file / guide | PDF pages |
| --- | --- | --- | --- |
| 01 | [LED blinking patterns](Practical-01-LED-Patterns/README.md) | [main.py](Practical-01-LED-Patterns/main.py) | 1-3 |
| 02 | [Control an LED using Telegram](Practical-02-Telegram-LED-Control/README.md) | [main.py](Practical-02-Telegram-LED-Control/main.py) | 4-10 |
| 03 | [Display the current time on TM1637](Practical-03-TM1637-Clock/README.md) | [main.py](Practical-03-TM1637-Clock/main.py) | 11-12 |
| 04 | [Read coordinates from a GPS module](Practical-04-GPS-Module/README.md) | [main.py](Practical-04-GPS-Module/main.py) | 13-16 |
| 05 | [Plot ADS1115 gas-sensor readings](Practical-05-ADS1115-Live-Plot/README.md) | [main.py](Practical-05-ADS1115-Live-Plot/main.py) | 17-20 |
| 06 | [Display text on a 16x2 I2C LCD](Practical-06-I2C-LCD/README.md) | [main.py](Practical-06-I2C-LCD/main.py) | 21-23 |
| 07 | [Read and write RFID tags](Practical-07-RFID-Read-Write/README.md) | [main.py](Practical-07-RFID-Read-Write/main.py) | 24-28 |
| 08 | [Enroll, search and delete fingerprints](Practical-08-Fingerprint-Management/README.md) | [main.py](Practical-08-Fingerprint-Management/main.py) | 29-38 |
| 09 | [Capture an image and video](Practical-09-Pi-Camera/README.md) | [main.py](Practical-09-Pi-Camera/main.py) | 39-41 |
| 10 | [Home automation using Flask](Practical-10-Home-Automation/README.md) | [app.py](Practical-10-Home-Automation/app.py) | 42-45 |
| 11 | [Show fingerprint match status on an LCD](Practical-11-Fingerprint-LCD/README.md) | [main.py](Practical-11-Fingerprint-LCD/main.py) | 46-50 |
| 12 | [Simulate a fingerprint door lock with a relay](Practical-12-Fingerprint-Relay/README.md) | [main.py](Practical-12-Fingerprint-Relay/main.py) | 51-56 |
| 13 | [MQTT publisher and LED subscriber](Practical-13-MQTT-Publish-Subscribe/README.md) | [subscriber.py](Practical-13-MQTT-Publish-Subscribe/subscriber.py) | 56-60 |
| 14 | [Control relays with a Flask dashboard](Practical-14-Flask-Dashboard/README.md) | [app.py](Practical-14-Flask-Dashboard/app.py) | 60-64 |
| 15 | [RFID and fingerprint two-factor demonstration](Practical-15-Two-Factor-Authentication/README.md) | [main.py](Practical-15-Two-Factor-Authentication/main.py) | 64-71 |
| 16 | [Camera motion detection with LCD feedback](Practical-16-Motion-Detection/README.md) | [main.py](Practical-16-Motion-Detection/main.py) | 71-76 |
| 17 | [Node-RED dashboard and push-button LED control](Practical-17-Node-RED-Dashboard/README.md) | [GUIDE.md](Practical-17-Node-RED-Dashboard/GUIDE.md) | 76-78 |
| 18 | [Monitor CPU, memory and temperature](Practical-18-System-Monitor/README.md) | [main.py](Practical-18-System-Monitor/main.py) | 78-82 |
| 19 | [RFID or fingerprint access control with logging](Practical-19-Access-Control-Logging/README.md) | [main.py](Practical-19-Access-Control-Logging/main.py) | 82-98 |
| 20 | [Windows IoT Core UWP demonstration](Practical-20-Windows-IoT-Core/README.md) | [MainPage.xaml.cs](Practical-20-Windows-IoT-Core/MainPage.xaml.cs) | 98-100 |

## How to use

1. Choose a practical in the table.
2. Read its wiring, requirements and correction notes.
3. Open the editable source file to study or copy into your own lab project.
4. Use source.pdf for the original procedure and any diagrams or screenshots supplied in the book.

Python programs require the matching Raspberry Pi hardware and dependencies. GitHub stores the files; it does not run GPIO or sensor programs. The Node-RED exercise is a guide because the PDF contains no flow export. The TM1637 driver and full UWP project are also not supplied.

The Python files have syntax checks; physical hardware and live services have not been tested here. See VALIDATION.md for the exact checks.

**Organized and maintained by [Shiven Dubey](https://github.com/Shiven-07).** Original reference material remains credited to its source; no authorship of the supplied book is claimed.

Also see: [.NET Core, C# & PWA practicals](https://github.com/Shiven-07/DotNet-Practicals).
