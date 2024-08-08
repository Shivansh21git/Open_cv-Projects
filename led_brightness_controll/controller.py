import pyfirmata

comport='COM5'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:10:p')

def led(bright):
    led_1.write(bright)
