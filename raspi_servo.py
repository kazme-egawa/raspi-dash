import pigpio
import sys

SERVO_PIN = 18
duty_min = 125
duty_max = 160

param = sys.argv
duty = int(param[1])
if (duty < duty_min):
    duty = duty_min
elif (duty > duty_max):
    duty = duty_max

pi = pigpio.pi()

pi.set_servo_pulsewidth(SERVO_PIN, duty)

pi.stop()
