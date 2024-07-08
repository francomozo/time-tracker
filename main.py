from time_tracker import StateMachine, InputOutputHandler, END_STATE_NAME


def main():
    io_handler = InputOutputHandler()
    sm = StateMachine()

    while sm.state.name != END_STATE_NAME:
        next_state = io_handler.listen_for_input(current_state_name=sm.state.name)
        prev_state_name, prev_state_elapsed_time = sm.switch_state(next_state)
        io_handler.log_state_time(prev_state_name, prev_state_elapsed_time)

    io_handler.show_todays_stats()
    print('End of the program')


if __name__ == '__main__':
    main()
