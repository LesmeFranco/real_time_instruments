from MPU6050 import MPU6050
from machine import Pin
import time
import math

mpu = MPU6050()

roll_offset = 0
pitch_offset = 0
calibrated = False
heading = 0.0
last_time = None

def calibrate_offsets():
    global roll_offset, pitch_offset, calibrated
    accel = mpu.read_accel_data()
    aX = accel["x"]
    aY = accel["y"]
    aZ = accel["z"]
    roll_offset = math.degrees(math.atan2(aY, aZ))
    pitch_offset = math.degrees(math.atan2(-aX, math.sqrt(aY**2 + aZ**2)))
    calibrated = True

calibrate_offsets()

def get_mpu_data():
    global heading, last_time

    # Leer datos
    accel = mpu.read_accel_data()
    aX = accel["x"]
    aY = accel["y"]
    aZ = accel["z"]

    gyro = mpu.read_gyro_data()
    gX = gyro["x"]
    gY = gyro["y"]
    gZ = gyro["z"]  # grados/segundo

    # Roll y pitch como antes
    roll = math.degrees(math.atan2(aY, aZ)) - roll_offset
    pitch = math.degrees(math.atan2(-aX, math.sqrt(aY**2 + aZ**2))) - pitch_offset

    # Integrar heading
    now = time.ticks_ms()
    if last_time is None:
        last_time = now
    dt = (time.ticks_diff(now, last_time)) / 1000.0  # segundos
    last_time = now

    heading += gZ * dt
    heading = heading % 360  # Mantener en [0, 360)

    return {
        "roll": roll,
        "pitch": pitch,
        "heading": heading,
        "AcX": aX,
        "AcY": aY,
        "AcZ": aZ
    }