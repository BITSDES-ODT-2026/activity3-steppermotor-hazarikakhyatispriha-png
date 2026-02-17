from machine import Pin
import time

mt1 = Pin(2,Pin.OUT)
mt2 = Pin(15,Pin.OUT)
mt3 = Pin(12,Pin.OUT)
mt4 = Pin(26,Pin.OUT)

dire = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
dire2 = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]

while True:
    print("halwe")
    for p in range(500):
        for i in dire:
            mt1.value(i[0])
            mt2.value(i[1])
            mt3.value(i[2])
            mt4.value(i[3])
            time.sleep_ms(5)
    print("wow")         
    for t in range(500):
        for l in dire2:
            mt1.value(l[0])
            mt2.value(l[1])
            mt3.value(l[2])
            mt4.value(l[3])
            time.sleep_ms(5)
    print("acha halwe")
