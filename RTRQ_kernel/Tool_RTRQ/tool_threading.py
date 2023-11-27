import time
import threading

class luong_timer():
    def __init__(self,time = 1,func= None) -> None:
        self.time   = time
        self.func   = func
        self.index  = 0

    def main(self):
        while (self.index == 1):
            time.sleep(self.time)
            self.func()
    
    def start(self):
        self.index  = 1
        self.thread = threading.Thread(target=self.main)
        self.thread.setDaemon(True)
        self.thread.start()
    
    def end(self):
        self.index  = 0
        del self.thread

class luong_basic():
    def __init__(self,func = None) -> None:
        self.func = func

    def main(self):
        if(self.func != None):
            self.func()
                
    def start(self):
        self.luong = threading.Thread(target=self.main)
        self.luong.setDaemon(True)
        self.luong.start()

    def end(self):
        del self.luong