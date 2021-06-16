import sys


from traffic import TrafficLightState, GreenState, RedState, \
                    YellowState, TrafficLightStateMachine, logger


if __name__ == '__main__':
    iterations = int(sys.argv[1])

    state_machine = TrafficLightStateMachine()
    runner = state_machine()

    for i, message in enumerate(runner):
        if i >= iterations:
            break
        logger.warning(f'The traffic light is: {message}')
