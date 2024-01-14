from multiprocessing import Process, Event, Value

import cv2

from ipc_states import SharedEventStateData
from ipc_states import GameState
from ipc_states import CameraState


class ImageCaptureProcess(Process):
    def __init__(self, shared_event: Event, device):
        super().__init__()
        self.event_state: SharedEventStateData = shared_event.event_state
        self.device = device
        self.cap = None

    def run(self):
        pass

    def quit(self):
        if self.cap:
            self.cap.release()
        self.cap = None

