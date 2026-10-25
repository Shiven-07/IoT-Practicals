# Source notes and corrections

The input is the supplied 100-page merged IoT practical book. IoT-Practical-Book.pdf is an unchanged copy. Each source.pdf preserves whole original pages.

Pages 56, 60, 64, 71, 76, 78, 82 and 98 contain boundaries between practicals, so those pages appear in both adjacent folders. The 20 extracts contain 108 page instances covering all 100 unique source pages.

source-text.txt is extracted reference text with trailing spaces removed, not executable code. Editable programs are deliberately repaired/adapted versions. Common changes include indentation, corrupted variable names, quotes and entry-point guards. Cleanup code, placeholder configuration and dependency lists are added. Per-practical details follow.

The source book contains missing images labeled Input IMAGE, blank result sections, copy/paste mistakes and incomplete setup steps. No absent output screenshot, driver, Node-RED flow or full Visual Studio project is presented as extracted content.

The Telegram token shown in the source screenshot is visibly masked. Programs contain no real token, chat ID, RFID allowlist or captured fingerprint templates. Generated media and local logs are excluded through .gitignore.

## Changes by practical

### 01

Restored the finally-block indentation; combined repeated output calls without changing the sequence.

### 02

Converted Python 2 print statements to Python 3; restored indentation; removed the undefined TelegramError block; stop now signals the main thread; added cleanup and a chat-ID allowlist. Uses the PDF legacy telepot library, whose live service compatibility has not been tested.

### 03

Restored indentation and removed repeated clearing. The PDF does not supply the driver. Packages sharing the tm1637 name can have different APIs; do not substitute blindly.

### 04

Restored indentation; added GNGGA support, malformed-sentence handling and no-fix handling. Source command spacing errors include ls /dev/serial*, cgps -s and gpsd /dev/serial0 -F /var/run/gpsd.sock. The daemon approach is an alternative, not a prerequisite for this direct-serial script.

### 05

Fixed plt/pit and y_vals capitalization, split joined statements and restored indentation. Updated the ADS1x15 imports/channel API to the upstream example. Set a 0-4.096 V plot scale matching gain 1; the configured scale is not permission to exceed the ADC supply/input limits. This slow plot is not a general-purpose oscilloscope.

### 06

Fixed Icd/lcd inconsistencies and the broken lcd.clear call; added clear/close cleanup.

### 07

Fixed RPI.GPIO capitalization and indentation. Clear now writes empty text rather than an undefined or previous text variable. Enable SPI; the source Serial instructions do not configure this SPI reader. Clearing text does not change the UID.

### 08

Reconstructed malformed functions, strings and method names (convertImage/createTemplate), corrected /dev/ttyUSB0 and hex values, restored the entry point, and added duplicate-enrollment return plus sensor-capacity validation. A generic USB fingerprint scanner is not automatically compatible with pyfingerprint.

### 09

Normalized the picam2 variable and replaced the invalid one-argument start_recording call with H264Encoder plus an output path. Added explicit still/video configuration and cleanup. Ignore copied RFID/fingerprint instructions in the source camera section.

### 10

Fixed __name__, the main guard, quotes and indentation. Added return links and output cleanup. This deliberately simple lab server has no login or CSRF protection; do not expose it publicly.

### 11

Normalized formatting, added a short polling delay and LCD cleanup. Use RPLCD with its i2c module; the source RPLCD-i2c package name is not required.

### 12

Moved the match decision inside the polling loop, restored indentation, added initial output state and shutdown cleanup. Polarity differs from Practical 19: configure it for the actual relay.

### 13

Separated publisher/subscriber files. Updated callback signatures to Paho API VERSION2 and constrained requirements to Paho 2.x. Added the publisher network loop and delivery wait; subscriber cleans up GPIO.

### 14

The PDF repeats the home-automation implementation under a dashboard aim. Both numbered folders are preserved. Added return links and cleanup; no production authentication is implied.

### 15

Repaired identifiers, indentation and the missing waiting-loop body. Uses BOARD numbering to agree with the RFID driver and avoid its BCM reset-pin ambiguity. No example UID is authorized by default. Added cleanup and a timeout. As in the source, any enrolled fingerprint can follow the configured card; it does not bind a particular finger to a particular card.

### 16

Repaired Picamera2/cv2 imports, dictionary syntax, names, indentation and LCD configuration. Chose RGB888 output with the documented OpenCV BGR interpretation; added camera/LCD cleanup. Lighting changes can trigger this simple detector.

### 17

No runnable flow has been invented or labeled as extracted. The guide records the required five-second override behavior and what must be supplied by the lab.

### 18

Repaired indentation, quotes and f-strings; replaced shell-based temperature reading with a bounded subprocess call and numeric parsing.

### 19

Reconstructed the damaged code, restored the absent main polling loop, corrected serial0/identifiers/strings, and made GPIO numbering consistently BOARD for the RFID driver. Added initial locked state and finally blocks that restore the relay after an interrupted pulse. Empty whitelist rejects all RFID tags until configured. This exercise is OR authentication, unlike Practical 15. It is a lab prototype, not a deployed door-security system.

### 20

Normalized the namespace to HelloIoT and formatting; added a minimal matching XAML page because InitializeComponent needs generated XAML support. The PDF supplies no full project or actual screenshots in its Input IMAGE placeholders. Do not assume that an image for an older Pi supports Raspberry Pi 4; confirm the lab board/image first.

## Documentation used to check adaptations

- [Picamera2 manual](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf): encoder/output API and frame formats.
- [Paho MQTT Python](https://eclipse.dev/paho/clients/python/docs/): callback API version and network loop.
- [ADS1x15 upstream example](https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15/blob/main/examples/ads1x15_simpletest.py): current imports and channel selection.
- [MFRC522 source](https://github.com/pimylifeup/MFRC522-python): default BOARD numbering and reader methods.
- [Raspberry Pi GPIO](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio): signal voltage and header functions.

Checked while preparing this package on 25 October 2026. Package installation and hardware compatibility were not tested here.
