def is_deterministic(automaton):
    """
    @breif : Checks if the given automaton is deterministic.
    @param : An instance of the Automata class.
    @return: True if deterministic, False otherwise.
    """
    # Condition 1: There must be exactly one initial state
    if len(automaton.initials) != 1:
        return False

    # Condition 2: No state should have multiple transitions for the same symbol

    for (state, symbol), next_state in automaton.transitions.items():
        if len(next_state)!=1:
            return False
    return True


def IsComplete(automaton):
    """
    @breif : check is an automaton is complete
    @param : the automaton class
    @return : True is complete False otherwise
    """
    if len(automaton.transitions) != len(automaton.alphabet)*len(automaton.states): #check is for each state and letter there is a transiton
        return False
    return True
