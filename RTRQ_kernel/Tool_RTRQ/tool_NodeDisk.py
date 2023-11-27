import sys
sys.path.append("./")

link_NodeText     = "FrontApp/Node_GUI/Node_Disk/Node_Text"
link_NodeImage    = "FrontApp/Node_GUI/Node_Disk/Node_Image"
link_NodeList     = "FrontApp/Node_GUI/Node_Disk/Node_List"
link_NodeEvent    = "FrontApp/Node_GUI/Node_Disk/Node_Event"
link_RunTimeEvent = "FrontApp/Node_GUI/Node_Disk/Node_Event/RunTime_Event.txt"
link_IndexFrame   = "FrontApp/Node_GUI/Node_Disk/Node_Text/Node_indexFrame.txt"
link_PositionFrame   = "FrontApp/Node_GUI/Node_Disk/Node_Text/Node_positionFrame.txt"


def create_file(link):
    f = open(link,"a")
    f.close()
    del f

def set_list_data(link,list):
    f = open(link,"w")
    for data in list:
        f.write(data + "\n")
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

def reset_file(link):
    f = open(link,"w")
    f.close()
    del f

def set_IndexFrame(index):
    set_file(link_IndexFrame,str(index))

def get_IndexFrame():
    index = int(get_file(link_IndexFrame))
    return index

def set_PositionApp(x,y):
    set_file(link_PositionFrame,str(x) + "," + str(y))
    
def get_PositionApp():
    data = get_file(link_PositionFrame)
    data = str(data).split("\n")[0].split(",")
    x = int(data[0])
    y = int(data[1])
    return x,y



class NodeText():
    def __init__(self,name) -> None:
        self.name = name
        self.link = link_NodeText + "/" + name
        create_file(self.link)
        None
    def create(self):
        create_file(self.link)

    def set(self,data):
        set_file(self.link,data)

    def get(self):
        data = get_file(self.link)
        return data

    def reset(self):
        reset_file(self.link)



class NodeEvent():
    def __init__(self,name) -> None:
        self.name = name
        self.link = link_NodeEvent + "/" + name
        create_file(self.link)
        None
    def create(self):
        create_file(self.link)

    def reset(self):
        reset_file(self.link)

    def call(self):
        set_file(link_RunTimeEvent,self.name)

class NodeImage():
    def __init__(self,name) -> None:
        self.name = name
        self.link = link_NodeImage + "/" + name
        create_file(self.link)
        None

    def create(self):
        create_file(self.link)

    def set(self,data):
        set_file(self.link,data)

    def get(self):
        data = get_file(self.link)
        return data

    def reset(self):
        reset_file(self.link)


class NodeList():
    def __init__(self,name) -> None:
        self.name = name
        self.link = link_NodeList + "/" + name
        create_file(self.link)
        None

    def create(self):
        create_file(self.link)

    def set(self,list):
        set_list_data(self.link,list)

    def get(self):
        list = get_list_data(self.link)
        return list

    def reset(self):
        reset_file(self.link)
            




        