import classAutomata as c

def isStandard(automata):
    """
    Checks if the given automaton is in standard form.
    An automaton is in standard form if it has exactly one initial state.
    
    Parameters:
    automata (Automata): The finite automaton to check.
    
    Returns:
    bool: True if the automaton is in standard form, False otherwise.
    """
    return len(automata.initials) == 1

def Standardize(automata):
    """
    Standardizes a given finite automaton.
    This function checks if the given automaton is already in standard form. 
    If it is, the function returns the automaton as is. 
    If it is not, the function creates a new initial state and adjusts the transitions accordingly to 
    standardize the automaton.
    
    Parameters:
    automata (Automata): The finite automaton to be standardized.
    
    Returns:
    Automata: A new finite automaton in standard form with a single initial state.
    
    Example:
    >>> automata = Automata(states, alphabet, transitions, initials, finals)
    >>> standardized_automata = Standardize(automata)
    """
    if isStandard(automata):
        # If the automaton is already in standard form, return it as is
        return automata
    else:
        # Create a new initial state
        newInitial = "I"
        # Copy the existing transitions
        newTransitions = automata.transitions.copy()
        # Adjust transitions to include the new initial state
        for (startState, letter), endState in automata.transitions.items():
            if startState in automata.initials:
                if (newInitial, letter) in automata.transitions:
                    # Add to existing set of transitions for the new initial state
                    newTransitions[(newInitial, letter)] += endState
                else:
                    # Create new set of transitions for the new initial state
                    newTransitions[(newInitial, letter)] = endState
        
        # Return a new automaton with the new initial state
        return c.Automata(automata.states, automata.alphabet, newTransitions, [newInitial], automata.finals, 1)