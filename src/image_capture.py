from multiprocessing import Process, Event, Value


class ImageCaptureProcess(Process):
    def __init__(self, device, capture_signal, quit_event):
        super().__init__()
        pass

    def run(self):
        pass

    def quit(self):
        pass
