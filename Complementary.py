import classAutomata as c

def Complementary(automaton):
    """
    Computes the complement of a given finite automaton.
    The complement of an automaton is a new automaton that recognizes the language that is not recognized by the original automaton.

    Args:
        automaton (Automata): The finite automaton for which to compute the complement.

    Returns:
        Automata: The automaton that recognizes the complement of the language recognized by the original automaton.
    """
    # Create a copy of the automaton
    new_automaton = automaton
    # Invert the set of final states
    new_automaton.finals = list(set(new_automaton.states) - set(new_automaton.finals))
    return new_automaton