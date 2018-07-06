"""
convenience utils
"""

import us


def format_state_name(state):
    """
    """
    return state.lower().replace(' ', '-')


def state_name_map():
    """
    """
    state_mapping = us.states.mapping('abbr', 'name')
    state_mapping = {k: format_state_name(v) for k, v in state_mapping.items()}
    return state_mapping


def state_file_info(filename):
    split = filename.split('.')[0].split('_')

    state = split[0]
    year = split[1]
    return state, year


def map_abbrev_to_state_key(abbrev):
    """
    e.g. NJ -> new-jersey
    """
    return state_name_map()[abbrev]
