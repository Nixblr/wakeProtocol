from pyWake.wake import Wake
import time
w = Wake('COM1')
w.open()
w.setAddress(0x10)
w.setCommand(3)
rx = w.io()
print("Received command: {}; Data: {}".format(hex(rx.getCommand()), 
                                              str(rx.getData(), encoding='ascii')))

for i in range(10):
    w.setCommand(15)
    w.clearData()
    w.addByte(1)
    w.io()
    time.sleep(0.5)
    
    w.setCommand(16)
    w.clearData()
    w.addByte(1)
    w.io()
    time.sleep(0.5)

    w.setCommand(15)
    w.clearData()
    w.addByte(0)
    w.io()
    time.sleep(0.5)

    w.setCommand(16)
    w.clearData()
    w.addByte(0)
    w.io()
    time.sleep(0.5)
w.close()