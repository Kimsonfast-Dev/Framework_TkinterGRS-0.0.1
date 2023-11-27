import sys
sys.path.append("./")

import tkinter as tk
from tkinter import *

import FrontApp.Extension_GUI.Extension_GUI_default.Default_element as Default_EF
import FrontApp.Tool_GUI.tool_NodeDisk   as tool_NodeDisk
import FrontApp.Tool_GUI.tool_NodeVisual as tool_NodeVisual

class obj_Frame():
    def __init__(self,obj_root):
        self.frame = tk.Frame(obj_root.root)
        self.frame.place(x=0,y=0,width = obj_root.w,height = obj_root.h)
        self.set_Frame(obj_root)
        self.set_node()
        self.set_Service(obj_root)

    def set_Frame(self,obj_root): 
        self.topbar = Default_EF.obj_topbar(obj_root) 
        self.topbar.set_title("Start")
        self.button = Default_EF.obj_button_close(obj_root)

    def set_node(self):
        None
    
    def set_Service(self,obj_root):
        None

    def close(self):
        self.frame.destroy()