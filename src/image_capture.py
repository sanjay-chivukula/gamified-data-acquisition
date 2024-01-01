from multiprocessing import Process, Event

import numpy as np

from data_models import CaptureSignalPayload
from data_models import ImageLabelData

import cv2

import constants


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
            payload: CaptureSignalPayload = self.capture_signal.payload

            payload.is_face_aligned = is_face_aligned(frame)
            if payload.is_capture and payload.is_face_aligned:
                label_data = ImageLabelData(
                    image=frame,
                    target_pos=payload.target_pos,
                    face_pos=(),
                    face_bounds=(),
                )
                store_data(label_data)
                payload.is_capture = False

        self.quit()

    def quit(self):
        if self.cap:
            self.cap.release()
        self.cap = None
        self.quit_event.set()


def preprocess_frame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(
        frame, (constants.IMAGE_HEIGHT, constants.IMAGE_WIDTH))
    return frame


def store_data(data: ImageLabelData):
    pass


def is_face_aligned(frame: np.ndarray) -> bool:
    pass
