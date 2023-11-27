import cv2

class obj_Camera():
    def __init__(self) -> None:
        self.video = None

    def open_camera(self):
        self.video = cv2.VideoCapture(0)

    def close_camera(self):
        self.video = None
    
    def kernel_camera(self):
        if(self.video != None):
            __,frame = self.video.read()
        return frame
    
    def test_camera(self):
        while 1:
            try:
                frame = self.kernel_camera()
                cv2.imshow("",frame)
                cv2.waitKey(1)
            except:
                None
    
