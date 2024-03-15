import time
import board
import adafruit_mcp9808
import busio
import adafruit_dht
import digitalio


def clean_up():
    power = digitalio.DigitalInOut(board.GP6)
    power.direction = digitalio.Direction.OUTPUT
    power.value=False
    
    power2 = digitalio.DigitalInOut(board.GP7)
    power2.direction = digitalio.Direction.OUTPUT
    power2.value=False
    return power, power2

def setup_devices():
    i2c = busio.I2C(scl=board.GP5, sda=board.GP4)
    i2c2 = busio.I2C(scl=board.GP15, sda=board.GP14)
    mcp = adafruit_mcp9808.MCP9808(i2c)
    mcp2 = adafruit_mcp9808.MCP9808(i2c2)
    dht = adafruit_dht.DHT22(board.GP3)
    return mcp, mcp2, dht

def led_ini():
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    return led

def blink(led):
    led.value = True
    time.sleep(1)
    led.value=False
    time.sleep(1)
    led.value=True
    time.sleep(0.5)
    led.value=False

if __name__ == '__main__':
    """Author: DeathRipper21"""
    power, power2 = clean_up()
    led=led_ini()
    print("Cleaning up....")
    time.sleep(2)
    power.value=True
    power2.value=True
    blink(led)
    mcp, mcp2, dht = setup_devices()
    print("Setting Devices...")
    blink(led)
    time.sleep(2)
    while True:
        try:
            temperature_c = dht.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dht.humidity
            print(f"DFRobot Sensor: Temperature {temperature_c} Humidity  {humidity}")
            tempC = mcp.temperature
            tempF = tempC * 9 / 5 + 32
            tempC2 = mcp2.temperature
            tempF2 = tempC2 * 9 / 5 + 32
            print(f"First Temperature: {tempC, tempF}")
            print(f"Second Temperature {tempC2, tempF2}")
            time.sleep(1)

        except RuntimeError as error:
            print("Error", error.args[0])
            time.sleep(1.0)
            continue
        except Exception as error:
            print(error)
            dht.exit()
            power.value=False
            power2.value=False
            raise error
        except KeyboardInterrupt as e:
            dht.exit()
            power.value=False
            power2.value=False
            raise e
