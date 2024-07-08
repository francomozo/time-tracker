from .state import State
from time_tracker.config.settings import IDLE_STATE_NAME, END_STATE_NAME


class StateMachine:
    """StateMachine Class"""
    def __init__(self):
        self.state = None
        self._set_state(IDLE_STATE_NAME)

    def switch_state(self, state_name):
        prev_state_elapsed_time = self.state.stop()
        prev_state_name = self.state.name

        self._set_state(state_name)
        return prev_state_name, prev_state_elapsed_time
    
    def _set_state(self, state_name):
        self.state = State(state_name)
        if self.state.name == END_STATE_NAME:
            return
        self.state.start()
