import pigpio

PWM_PIN = [23, 24]
FREQ = 100
RANGE = 255

pi = pigpio.pi()

for i in range(2):
    pi.set_mode(PWM_PIN[i], pi.gpio.OUTPUT)
    pi.set_PWM_frequency(PWM_PIN[i], FREQ)
    pi.set_PWM_range(PWM_PIN[i], RANGE)

mae = pi.get_PWM_dutycycle(PWM_PIN[0])
ushiro = pi.get_PWM_dutycycle(PWM_PIN[1])

if (mae == 0):
    ushiro += 50
    if (ushiro > 250):
        ushiro = 250
else:
    mae -= 50
    if (mae < 0):
        ushiro -= mae
        mae = 0


pi.set_PWM_dutycycle(PWM_PIN[0], mae)
pi.set_PWM_dutycycle(PWM_PIN[1], ushiro)
