import time


class State:
    def __init__(self, name):
        self.name = name
        self._start_time = None

    def _start_timer(self):
        self._start_time = time.time()

    def _stop_timer(self):
        if self._start_time:
            elapsed_time = time.time() - self._start_time
            self._start_time = None
            return elapsed_time
        return 0

    def start(self):
        self._start_timer()

    def stop(self):
        elapsed_time = self._stop_timer()
        return elapsed_time