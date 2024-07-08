import json
import os
from datetime import datetime
from pathlib import Path

from .simple_term_menu import TerminalMenu
from time_tracker.config import get_states, TIMELOG_FILE


class InputOutputHandler:
    """InputOutputHandler class"""
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self._timelog_file_path = Path.home() / TIMELOG_FILE
        self._timelog = self._load_timelog_file()
        self._all_opts = get_states()

    def listen_for_input(self, current_state_name):
        opts = [opt for opt in self._all_opts if opt != current_state_name]
        menu = TerminalMenu(opts, title=f'Current State: {current_state_name}')
        menu_entry_index = menu.show()
        return opts[menu_entry_index]

    def log_state_time(self, state_name, elapsed_time):
        """Log the time spent on a state."""
        current_date = datetime.now().strftime('%Y/%m/%d')
        elapsed_time_hours = self._convert_seconds_to_hours(elapsed_time)
        self._timelog.setdefault(current_date, {})
        self._timelog[current_date][state_name] = self._timelog[current_date].get(state_name, 0) + elapsed_time_hours
        self._save_timelog_file()

    def show_todays_stats(self):
        current_date = datetime.now().strftime('%Y/%m/%d')
        todays_timelog = {
            k: self._hours_float_to_hours_minutes(v)
            for k, v in self._timelog[current_date].items()
        }
        print(f'Today\'s stats ({current_date}):')
        print(json.dumps(todays_timelog, indent=4))  # TODO convert to hs-mis (ie 1h30m)

    def _load_timelog_file(self):
        if not self._timelog_file_path.exists():
            self._timelog_file_path.parent.mkdir(parents=True, exist_ok=True)
            return {}
        with open(self._timelog_file_path, 'r') as f:
            return json.load(f)

    def _save_timelog_file(self):
        with open(self._timelog_file_path, 'w') as f:
            json.dump(self._timelog, f, indent=4)

    @staticmethod
    def _convert_seconds_to_hours(elapsed_time_seconds):
        total_minutes = elapsed_time_seconds // 60

        hours = total_minutes // 60
        minutes = total_minutes % 60

        hours_float = hours + (minutes / 60)
        return hours_float

    @staticmethod
    def _hours_float_to_hours_minutes(hours_float):
        hours = int(hours_float)
        minutes = int((hours_float - hours) * 60)
        return f'{hours}h{minutes}m'