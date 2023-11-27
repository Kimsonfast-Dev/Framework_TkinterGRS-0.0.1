import sys
import os
sys.path.append("./")

link_NodeEvent = "FrontApp/Node_GUI/Node_Disk/Node_Event"
link_NodeImage = "FrontApp/Node_GUI/Node_Disk/Node_Image"
link_NodeList  = "FrontApp/Node_GUI/Node_Disk/Node_List"
link_NodeText  = "FrontApp/Node_GUI/Node_Disk/Node_Text"



def create_file(link):
    f = open(link,"a")
    f.close()
    del f

def set_file(link,data):
    f = open(link,"w")
    f.write(data)
    f.close()
    del f

def copy_file(name,link_originfile):
    link =  name + ".py"
    open(link,"a").close()
    f      = open(link_originfile,"r")
    f_copy = open(link,"w")
    for data in f:
        f_copy.write(data)
    f.close()
    f_copy.close()
    del f
    del f_copy

def delete_file(name):
    name = name + ".py"
    os.remove(name)


def clear_folder(link_folder):
    list_file = os.listdir(link_folder)
    for file in list_file:
        try:
            str(file).split(".")[1]
        except:
            link_file = link_folder + "/" + file
            print(link_file)
            os.remove(link_file)
    

class CommandLine():
    def __init__(self) -> None:
        self.link_source = "FrontApp/Frame_GUI"
        None

    def main_CommandLine(self):
        self.command = input("FontApp Line User : ")
        self.line = self.command.split(" ")[0]
        self.data = self.command.split(" ")
        del self.data[0]
        self.mg_CommandLine(self.line,self.data)

    def mg_CommandLine(self,line,data):
        if   (line == "create"): self.createFrame(data)
        elif (line == "delete"): self.deleteFrame(data)
        elif (line == "ReNode"): self.clear_Node()
        elif (line == "close"): os.system("CLS")
        elif (line == "clear"): os.system('CLS')
        else: print("Not Command")

    def createFrame(self,data):
        for name in data:
            name = self.link_source + "/" + name
            copy_file(name,"FrontApp/Extension_GUI/Extension_GUI_Template/framebasic.py")

    def deleteFrame(self,data):
        for name in data:
            name = self.link_source + "/" + name
            delete_file(name)


    def clear_Node(self):
        clear_folder(link_NodeEvent)
        clear_folder(link_NodeList)
        clear_folder(link_NodeText)
        clear_folder(link_NodeImage)
        

