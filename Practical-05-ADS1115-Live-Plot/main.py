"""Slow voltage plot, adapted to the current ADS1x15 library API."""
import time
from collections import deque
import board
import matplotlib.pyplot as plt
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15

def main():
    i2c = board.I2C()
    ads = ADS1115(i2c)
    ads.gain = 1
    channel = AnalogIn(ads, ads1x15.Pin.A0)
    x_values, y_values = deque(maxlen=50), deque(maxlen=50)
    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot([], [], marker="o", label="ADS1115 channel A0")
    ax.set(title="MQ2 Gas Sensor Live Plot", xlabel="Sample",
           ylabel="Voltage (V)", ylim=(0, 4.096))
    ax.legend()
    counter = 0
    try:
        while plt.fignum_exists(fig.number):
            x_values.append(counter)
            y_values.append(channel.voltage)
            line.set_data(x_values, y_values)
            ax.set_xlim(max(0, counter - 49), max(1, counter))
            fig.canvas.draw_idle()
            plt.pause(1.0)
            counter += 1
    except KeyboardInterrupt:
        pass
    finally:
        plt.close(fig)
        i2c.deinit()

if __name__ == "__main__":
    main()
