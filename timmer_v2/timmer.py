import time
import threading

class timmer(threading.Thread):
    def __init__(self, hour=None, minute=None):
        super(timmer, self).__init__()
        self.running = False
        self.hour = hour
        self.minute = minute

    def stop(self):
        self.running = False

    def run(self) -> None:
        self.running = True
        s = int(self.hour) * 3600 + int(self.minute) * 60
        while self.running and s != 0:
            time.sleep(1)
            s -= 1
        self.running = False
