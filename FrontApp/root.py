import sys
sys.path.append("./")

import tkinter as tk
import FrontApp.Tool_GUI.tool_NodeDisk   as Tool_NodeDisk
import FrontApp.Tool_GUI.tool_NodeVisual as Tool_NodeVisual

import FrontApp.Frame_GUI.Frame_Start as Frame_Start

class obj_root():
    def __init__(self,w,h):
        self.set_root(w,h)

###################################### START FRONTER ######################################################
    def setup_GUI(self):
        self.create_frame(Frame_Start)

    def update_Frame(self):
        try:
            index = Tool_NodeDisk.get_IndexFrame()
            if(index != self.root_indexPage):
                self.root_indexPage = index
                if   (self.root_indexPage == 1)   : self.move_frame(Frame_Start)
                if   (self.root_indexPage == 2)   : None
                if   (self.root_indexPage == 3)   : None
                if   (self.root_indexPage == 3)   : None
                elif (self.root_indexPage == 999) : self.close()
                else                            : None
        except:
            print("error app")
            None

######################################## END FRONTER  ######################################################

    def run(self):
        #self.root.wm_attributes('-fullscreen', 'True')
        #self.root.attributes("-topmost", True)  
        self.root.overrideredirect(True);   
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.mainloop()

    def close(self):
        self.root.destroy()

    def set_root(self,w,h):
        self.root = tk.Tk()
        self.w = w
        self.h = h
        self.size_Frame(self.w,self.h)
        self.setup_GUI()
        self.setup_service()
        None

    def update_root(self,time=1000,func=None):
        def root_func(): 
            if(func!=None): func()
            self.root.after(time,lambda:root_func())
        self.root.after(time,lambda:root_func())

    def setup_service(self):
        Tool_NodeDisk.set_IndexFrame(0)
        self.root_indexPage = 0
        self.update_root(100,self.update_Frame)

    def size_Frame(self,Tk_Width,Tk_Height):
        self.width = Tk_Width
        self.height = Tk_Height
        x_Left = int(self.root.winfo_screenwidth()/2 - Tk_Width/2)
        y_Top = int(self.root.winfo_screenheight()/2 - Tk_Height/2)
        self.root.geometry("{}x{}+{}+{}".format(self.w,self.h,x_Left, y_Top))
        x,y = Tool_NodeDisk.get_PositionApp()
        self.root.geometry("{}x{}+{}+{}".format(Tk_Width,Tk_Height,x, y))

    def move(self,event):
        x = event.x_root - self.deltax
        y = event.y_root - self.deltay
        self.root.geometry(f'+{x}+{y}')
        Tool_NodeDisk.set_PositionApp(x,y)

    def delta(self,event):
        self.deltax = event.x_root - self.root.winfo_x()
        self.deltay = event.y_root - self.root.winfo_y()

    def create_frame(self,page_Frame):
        self.obj_Frame = page_Frame.obj_Frame(self)

    def remove_frame(self):
        self.obj_Frame.close()
        del self.obj_Frame
    
    def move_frame(self,page_Frame):
        self.remove_frame()
        self.create_frame(page_Frame)

def show():  
    app = obj_root(1000,510)
    app.run()
    sys.exit()

###################        DEV_ENVIRONMENT      ################################################
# import hupper
# def start_reloader():
#     hupper.start_reloader('root.main')
# if __name__ == "__main__":
#     start_reloader()

#####################         MAIN CODE       #################################################
#show()