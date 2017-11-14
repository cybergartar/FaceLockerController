from control import Relay
from control import Speaker
import time

relay = Relay()
sp = Speaker()

for i in range(1, 5):
    sp.beep(0.1)
    time.sleep(0.1)
    sp.beep(0.1)
    time.sleep(0.5)
    relay.set(i, 0)
    time.sleep(1)
    relay.set(i, 1)
    time.sleep(0.5)
