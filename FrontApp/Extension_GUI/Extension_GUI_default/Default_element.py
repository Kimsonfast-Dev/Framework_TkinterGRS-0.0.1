import sys
sys.path.append("./")

import tkinter as tk
from tkinter import *

import time
import threading

class obj_topbar():
    def __init__(self,obj_root) -> None:
        self.topbar = tk.Label(obj_root.root)
        self.topbar.place(x=0,y=0,width=obj_root.w,height=30)
        self.topbar.bind('<Button-1>',obj_root.delta)
        self.topbar.bind('<B1-Motion>',obj_root.move)
        self.set_bg("Blue")
        self.set_fg("white")

    def set_title(self,name):
        self.topbar.configure(text=name)
        self.topbar.configure(font=("Times New Roman", 15, "bold"))
    
    def set_bg(self,bg):
        self.topbar.configure(background=bg)

    def set_fg(self,fg):
        self.topbar.configure(fg=fg)
    
    def close(self):
        self.topbar.destroy()

class obj_button_close():
    def __init__(self,obj_root):
        self.topbar = tk.Button(obj_root.root)
        self.topbar.place(x=obj_root.w-30,y=0,width=30,height=30)
        self.topbar.configure(command=obj_root.close)
        self.topbar.configure(borderwidth=0,activebackground="Blue")
        self.set_icon("FrontApp/Extension_GUI/Extension_GUI_default/Media/Icon/ButtonClose_#1.png")
        self.set_background("Blue")

    def set_icon(self,link):
        self.icon = PhotoImage(file=link)
        self.topbar.configure(image=self.icon)

    def set_background(self,bg):
        self.topbar.configure(background=bg)

    def close(self):
        self.topbar.destroy()

class box_element():
    def __init__(self,obj_frame) -> None:
        self.box = tk.Label(obj_frame.frame)
        self.frame = obj_frame.frame
        self.sw_animation_Into   = False
        self.sw_animation_Leave  = False
        self.sw_animation_Click1 = False
        self.sw_animation_Click2 = False
        self.sw_animation_Click3 = False
        self.include_event()
        self.reset_event()
    
    def include_event(self):
        self.box.bind("<Button-1>" , self.get_EventClick1)
        self.box.bind("<Button-2>" , self.get_EventClick2)
        self.box.bind("<Button-3>" , self.get_EventClick3)
        self.box.bind("<B1-Motion>", self.get_EventMotion1)
        self.box.bind("<B2-Motion>", self.get_EventMotion2)
        self.box.bind("<B3-Motion>", self.get_EventMotion3)
        self.box.bind("<Leave>"    , self.get_EventLeave)
        self.box.bind("<Enter>"    , self.get_EventInto)

    def show_event(self):
        self.func_EventClick1  = functools.partial(print,"EV_click1")
        self.func_EventClick2  = functools.partial(print,"EV_click2")
        self.func_EventClick3  = functools.partial(print,"EV_click3")
        self.func_EventMotion1 = functools.partial(print,"EV_motion1")
        self.func_EventMotion2 = functools.partial(print,"EV_motion2")
        self.func_EventMotion3 = functools.partial(print,"EV_motion3")
        self.func_EventLeave   = functools.partial(print,"EV_leave")
        self.func_EventInto    = functools.partial(print,"EV_into")

    def reset_event(self):
        self.func_EventClick1  = None
        self.func_EventClick2  = None
        self.func_EventClick3  = None
        self.func_EventMotion1 = None
        self.func_EventMotion2 = None
        self.func_EventMotion3 = None
        self.func_EventLeave   = None
        self.func_EventInto    = None

    def set_EventClick1(self,func)  : self.func_EventClick1  = func
    def set_EventClick2(self,func)  : self.func_EventClick2  = func
    def set_EventClick3(self,func)  : self.func_EventClick3  = func
    def set_EventMotion1(self,func) : self.func_EventMotion1 = func
    def set_EventMotion2(self,func) : self.func_EventMotion2 = func
    def set_EventMotion3(self,func) : self.func_EventMotion3 = func
    def set_EventLeave(self,func)   : self.func_EventLeave   = func
    def set_EventInto(self,func)    : self.func_EventInto    = func

    def get_EventClick1(self,event) : 
        if(self.sw_animation_Click1 == True): self.animation_Click(0.1)
        if(self.func_EventClick1 != None): self.func_EventClick1()

    def get_EventClick2(self,event) :
        if(self.sw_animation_Click2 == True): self.animation_Click(0.1) 
        if(self.func_EventClick2 != None): self.func_EventClick2()

    def get_EventClick3(self,event) : 
        if(self.sw_animation_Click3 == True): self.animation_Click(0.1)
        if(self.func_EventClick2 != None): self.func_EventClick3()

    def get_EventMotion1(self,event): 
        if(self.func_EventMotion1 != None): self.func_EventMotion1()

    def get_EventMotion2(self,event): 
        if(self.func_EventMotion2 != None): self.func_EventMotion2()

    def get_EventMotion3(self,event): 
        if(self.func_EventMotion3 != None): self.func_EventMotion3()

    def get_EventLeave(self,event)  :
        if(self.sw_animation_Leave == True): self.animation_Leave()
        if(self.func_EventLeave != None): self.func_EventLeave()

    def get_EventInto(self,event)   : 
        if(self.sw_animation_Into == True): self.animation_Into()
        if(self.func_EventInto != None): self.func_EventInto()

    def animation_Click(self,ti):
        def animation_Click():
            try:
                self.box.configure(bg = "white")
                time.sleep(ti)
                self.box.configure(bg = self.bg)
            except:
                None
        self.thread = threading.Thread(target=animation_Click).start()
    
    def animation_Into(self):
        self.box.configure(bg = "white")

    def animation_Leave(self):
        self.box.configure(bg = self.bg)

    def set_position(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.box.place(x=x,y=y,width=w,height=h)

    def set_bg(self,bg):
        self.bg = bg
        self.box.configure(bg = bg)

    def set_fg(self,fg):
        self.box.configure(fg=fg)

    def set_font(self,font):
        self.box.configure(font=font)

    def set_title(self,text):
        self.box.configure(text=text)

    def set_icon(self,link):
        self.icon = PhotoImage(file = self.icon)
        self.box.configure(image=self.icon)

    def set_icon_model(self,link):
        from PIL import Image, ImageTk
        self.icon = Image.open(link)
        self.icon = self.icon.resize((self.w,self.h))
        self.icon = ImageTk.PhotoImage(self.icon)
        self.box.configure(image=self.icon)

    def set_video(self,image_opencv):
        import cv2
        from PIL import Image, ImageTk
        try:
            self.icon = cv2.cvtColor(image_opencv,cv2.COLOR_BGR2RGB)
            self.icon = Image.fromarray(self.icon)
            self.icon = self.icon.resize((self.w,self.h))
            self.icon = ImageTk.PhotoImage(self.icon)
            self.box.configure(image=self.icon)
        except:
            None

    def update_data(self,time=1000, function = None):
        def update():
            if(function != None): function()
            self.box.after(time,lambda:update())
        self.box.after(time,lambda:update())