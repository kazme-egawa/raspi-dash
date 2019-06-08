import pigpio

SERVO_PIN = 18
duty_min = 1250
duty_max = 1600

pi = pigpio.pi()
duty = pi.get_servo_pulsewidth(SERVO_PIN)
duty -= 30

if (duty < duty_min):
    duty = duty_min
elif (duty > duty_max):
    duty = duty_max

pi.set_servo_pulsewidth(SERVO_PIN, duty)

pi.stop()
