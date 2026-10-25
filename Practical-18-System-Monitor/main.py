import subprocess
import time
import psutil

def cpu_temperature():
    try:
        reading = subprocess.check_output(
            ["vcgencmd", "measure_temp"], text=True, timeout=2).strip()
        return float(reading.removeprefix("temp=").removesuffix("'C"))
    except (OSError, subprocess.SubprocessError, ValueError):
        return None

def main():
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            temperature = cpu_temperature()
            print("\nRaspberry Pi Monitoring")
            print(f"CPU Usage: {cpu}%")
            print(f"Memory Usage: {memory}%")
            print("CPU Temperature:",
                  "unavailable" if temperature is None else f"{temperature:.1f} C")
            time.sleep(2)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
