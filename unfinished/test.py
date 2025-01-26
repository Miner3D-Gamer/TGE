import psutil
import time
# secsleft
def is_battery_charging():
    battery = psutil.sensors_battery()
    return battery.power_plugged
def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent
def second_until_fully_charged():
    battery = psutil.sensors_battery()
    return battery.secsleft

def seconds_since_boot():
    return time.time()-psutil.boot_time()

