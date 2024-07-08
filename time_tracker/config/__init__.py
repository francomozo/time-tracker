import os
import json

from .settings import DEFAULT_STATES, MY_STATES_JSON_FILE, TIMELOG_FILE

def get_states():
    config_file = os.path.join(os.path.dirname(__file__), MY_STATES_JSON_FILE)
    with open(config_file, 'r') as f:
        custom_states = json.load(f)

    return [
        DEFAULT_STATES[0],
        *custom_states,
        DEFAULT_STATES[1]
    ]