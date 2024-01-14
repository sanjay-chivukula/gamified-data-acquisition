from multiprocessing import Process, Manager, Event


class GameProcess(Process):
    def __init__(self, shared_event: Event):
        super().__init__()
        pass

    def run(self):
        pass

    def quit(self):
        pass
