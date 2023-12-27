from multiprocessing import Process, Event

import cv2


class ImageCaptureProcess(Process):
    def __init__(self, device, capture_signal, quit_event):
        super().__init__()
        self.device = device
        self.capture_signal = capture_signal
        self.quit_event = quit_event
        self.cap = None

    def run(self):
        self.cap = cv2.VideoCapture()

        while not self.quit_event.is_set():
            ret, frame = self.cap.read()
            pass

        self.quit()

    def quit(self):
        if self.cap:
            self.cap.release()
        self.cap = None
        self.quit_event.set()
