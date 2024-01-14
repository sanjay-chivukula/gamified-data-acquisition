from multiprocessing import Process, Event, Value

import cv2

from ipc_states import SharedEventStateData
from ipc_states import GameState
from ipc_states import CameraState
from ipc_states import FaceState


class ImageCaptureProcess(Process):
    def __init__(self, shared_event: Event, device):
        super().__init__()
        self.event_state: SharedEventStateData = shared_event.event_state
        self.device = device
        self.cap = None

    def run(self):
        self.init_camera()

        while self.event_state.game_state != GameState.QUIT:
            ret, frame = self.cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            self.event_state.face_state = self.face_detect(frame)
            if self.event_state.is_capture:
                if self.event_state.face_state == FaceState.VISIBLE:
                    self.write_data(frame)
                    self.event_state.is_capture = False
                    self.event_state.target_pos = None

        self.quit()

    def quit(self):
        if self.cap:
            self.cap.release()
        self.cap = None

    def init_camera(self):
        if not self.cap:
            self.cap = cv2.VideoCapture(self.device)
            if self.cap:
                self.event_state.camera_state = CameraState.AVAILABLE

    def face_detect(self, frame):
        return FaceState.VISIBLE if frame else FaceState.NOT_VISIBLE

    def write_data(self, frame):
        pass
