from plyer import notification as n
import time
while 1:
    time.sleep(5)
    n.notify(title="Drink your Water",
             message="Please leave your work and drink water!!",
             
             timeout=12)
