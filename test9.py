from pyfirmata import Arduino, SERVO, util
from time import sleep

port='COM3'
pin=9
board=Arduino(port)

board.digital[pin].mode=SERVO

def rotateservo(pin, angle):
    board.digital[pin].write(angle)
    print("moved")
    sleep(1)

while True:
    x=input("input")

    if x=='1':
        for i in range(0,180):
            rotateservo(pin,i)

    elif x=='2':
        for i in range(0, 90):
            rotateservo(pin,i)
    elif x=='3':
        for i in range(0,45):
            rotateservo(pin,i)