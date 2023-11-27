import sys
sys.path.append("./")

import RTRQ_kernel.Tool_RTRQ.tool_threading      as tool_threading
import RTRQ_kernel.Tool_RTRQ.tool_data_NodeGUI   as tool_data_NodeGUI
import RTRQ_kernel.app as app

class Runtime_APP():
    def __init__(self) -> None:
        self.app = app.APP()
        self.timer_event_Runtime  = tool_threading.luong_timer(0.001,self.Event_Runtime)

    def run(self):
        self.timer_event_Runtime.start()

    def close(self):
        self.app.close()
        del self.app
        del self.timer_event_Runtime

    def Event_Runtime(self):
        event = tool_data_NodeGUI.read_event()
        if(event != "*"):tool_threading.luong_basic(self.app.Mg_event(event)).start()
