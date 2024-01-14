from multiprocessing import Process, Event, Value


class ImageCaptureProcess(Process):
    def __init__(self, shared_event: Event, device):
        super().__init__()
        pass

    def run(self):
        pass

    def quit(self):
        pass
