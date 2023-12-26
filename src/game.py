from multiprocessing import Process, Manager, Event


class GameProcess(Process):
    def __init__(self, capture_signal, quit_event):
        super().__init__()
        pass

    def run(self):
        pass

    def quit(self):
        pass
