import serial
import serial.tools.list_ports
import threading

global data_read
data_read = None

class obj_serial():
    global data_read
    def __init__(self) -> None:
        self.root = serial.Serial()
        self.status = None
        self.list_serial = None
        self.portname  = None
        self.baudrate  = None
        self.data_read = None
        self.func = None

    def get_list(self):
        ports = []
        for port in serial.tools.list_ports.comports():
            ports.append(port.name)
        self.list_serial = ports
        return ports
    
    
    def open(self,portname,baudrate):
        if(self.root.is_open==0):
            self.portname = portname
            self.baudrate = baudrate
            self.root.port = self.portname
            self.root.baudrate = self.baudrate
            self.root.open()
            self.timer = threading.Thread(target=self.main_loop).start()
        else: 
            print("warning : Connecting")
    
    def close(self): 
        if(self.root.is_open== 1): self.root.close()

    def read(self):
        if (self.root.is_open == 1): data = self.root.readline().decode().split("\r\n")[0]
        return data

    def send(self,data):
        data = str(data).encode()
        self.root.write(data)

    def main_loop(self):
        global data_read
        while self.root.is_open:
            try:
                data = self.read()
                if(data != self.data_read): 
                    data_read = data
                    self.data_read = data
                    self.func()
            except:
                None

    def event_read(self,func=None):
        self.func = func

    def change(self,portname,buadrate):
        self.close()
        self.open(portname,buadrate)

    def checkout(self):
        if(self.root.is_open): print("connecting")
        else:                  print("not connecting")

def print_hu():
    print("hello")

def test():
    import os
    he = obj_serial()
    he.event_read(print_hu)
    while 1:
        try:
            data = input("command : ")
            data = data.split(" ")
            if  (data[0] == "start"): he.open(data[1],int(data[2]))
            elif(data[0] == "p")    : print(data_read)
            elif(data[0] == "send") : he.send(data[1])
            elif(data[0] == "check"): he.checkout()
            elif(data[0] == "close"): he.close()
            elif(data[0] == "show") : print(he.get_list())
            elif(data[0] == "break"): 
                os.system("CLS")
                break
            elif(data[0] == "clr"  ): os.system("CLS")
            else: None
        except:
            None
