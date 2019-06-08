import pigpio

PWM_PIN = [23, 24]
FREQ = 100
RANGE = 255

pi = pigpio.pi()

for i in range(2):
    pi.set_mode(PWM_PIN[i], pi.gpio.OUTPUT)
    pi.set_PWM_frequency(PWM_PIN[i], FREQ)
    pi.set_PWM_range(PWM_PIN[i], RANGE)

pi.set_PWM_dutycycle(PWM_PIN[0], 250)
pi.set_PWM_dutycycle(PWM_PIN[1], 0)
