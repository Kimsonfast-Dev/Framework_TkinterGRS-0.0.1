import sys
sys.path.append("./")

import RTRQ_kernel.Tool_RTRQ.tool_data_NodeGUI as tool_NodeGUI
tool_NodeGUI.MG_NodeGUi().update_data()

import RTRQ_kernel.Tool_RTRQ.tool_threading      as tool_threading
import RTRQ_kernel.Data_RTRQ.Node_GUI.Node_Event as Data_NodeEvent
import RTRQ_kernel.Data_RTRQ.Node_GUI.Node_List  as Data_NodeList
import RTRQ_kernel.Data_RTRQ.Node_GUI.Node_Text  as Data_NodeText
import RTRQ_kernel.Data_RTRQ.Node_GUI.Node_Image as Data_NodeImage
import RTRQ_kernel.Tool_RTRQ.tool_NodeDisk       as tool_NodeDisk
import RTRQ_kernel.Tool_RTRQ.tool_NodeVisual     as tool_NodeVisual

import ServiceApp.service_Serial.main as uart
import ServiceApp.service_Camera.main as Camera

class APP():
    def __init__(self):
        None

    def close(self):
        None

    def Mg_event(self,event):
        None

        