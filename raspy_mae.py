import pigpio

pwm_pin = [23, 24]
freq = 100
range = 255

pi = pigpio.pi()

for i in range(2):
    pi.set_mode(pwm_pin[i], pi.gpio.OUTPUT)
    pi.set_PWM_frequency(pwm_pin[i], freq)
    pi.set_PWM_range(pwm_pin[i], range)

mae = pi.get_PWM_dutycycle(pwm_pin[0])
ushiro = pi.get_PWM_dutycycle(pwm_pin[1])

if (ushiro == 0):
    mae += 50
    if (mae > 250):
        mae = 250
else:
    ushiro -= 50
    if (ushiro < 0):
        mae -= ushiro
        ushiro = 0


pi.set_PWM_dutycycle(pwm_pin[0], mae)
pi.set_PWM_dutycycle(pwm_pin[1], ushiro)
