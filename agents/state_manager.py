current_state = {}


def set_state(key, value):

    current_state[key] = value


def get_state(key):

    return current_state.get(key)