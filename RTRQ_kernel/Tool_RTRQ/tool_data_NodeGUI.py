import sys
import os
sys.path.append("./")

link_Node_FrontApp = "FrontApp/Node_GUI/Node_Disk"
link_Node_Kernel   = "RTRQ_kernel/Data_RTRQ/Node_GUI"

def show_file(link_folder):
    list_file = os.listdir(link_folder)
    return list_file

def set_list_data(link,list):
    f = open(link,"w")
    for data in list:
        try:
            str(data).split(".")[1]
        except:
            line = data + "=" + '"' + data + '"'
            f.write(line + "\n")
    f.close()
    del f

def get_list_data(link):
    f = open(link,"r")
    list = []
    for data in f:
        data = str(data).split("\n")[0]
        list.append(data)
    f.close()
    del f
    return list

def set_file(link,data):
    f = open(link,"w")
    f.write(data)
    f.close()
    del f
    

def get_file(link):
    f = open(link,"r")
    data = f.readline()
    f.close()
    del f
    return data


def create_file(link):
    f = open(link,"a")
    f.close()
    del f

def reset_file(link):
    f = open(link,"w")
    f.close()
    del f


class MG_NodeGUi():
    def __init__(self) -> None:
        None

    def update_obj(self,name):
        link_input  = link_Node_FrontApp + "/" + name
        link_output = link_Node_Kernel + "/" + name + ".py"
        list_event = show_file(link_input)
        create_file(link_output)
        set_list_data(link_output,list_event)


    def update_data(self):
        self.update_obj("Node_Event")
        self.update_obj("Node_Text")
        self.update_obj("Node_Image")
        self.update_obj("Node_List")

def read_event():
    link = "FrontApp/Node_GUI/Node_Disk/Node_Event/RunTime_Event.txt"
    data = "*"
    event = get_file(link)
    if(event != ""):
        data = event
        reset_file(link)
    return data
