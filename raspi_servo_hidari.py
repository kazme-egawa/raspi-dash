import pigpio

SERVO_PIN = 18
duty_min = 125
duty_max = 160

duty = pi.get_servo_pulsewidth(SERVO_PIN)
duty -= 5

if (duty < duty_min):
    duty = duty_min
elif (duty > duty_max):
    duty = duty_max

pi = pigpio.pi()

pi.set_servo_pulsewidth(SERVO_PIN, duty)

pi.stop()
