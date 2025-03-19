import classAutomata as c
import Deterministic as d

def IsComplete(automaton):
    """
    Check if a given finite automaton is complete.

    A finite automaton is considered complete if it is deterministic and for each state and letter in the alphabet, there is a corresponding transition.

    Args:
        automaton (Automaton): The finite automaton to check. 

    Returns:
        bool: True if the automaton is complete, False otherwise.
    """
    # Check if the automaton is deterministic and if the number of transitions equals the product of the number of states and the number of letters in the alphabet
    return d.is_deterministic(automaton) and len(automaton.transitions) == len(automaton.alphabet)*len(automaton.states)

def CompleteAutomata(automaton):
    """
    Completes a given finite automaton by ensuring it is deterministic and adding missing transitions.

    If the automaton is already complete, it returns the original automaton.
    If the automaton is not deterministic, it first determinizes the automaton.
    Then, it adds a new state "P" and ensures that every state has a transition for every letter in the alphabet.
    Missing transitions are directed to the new state "P".

    Args:
        automaton (Automata): The finite automaton to be completed.

    Returns:
        Automata: The complete deterministic finite automaton.
    """
    # Check if the automaton is already complete
    if IsComplete(automaton):
        print("Automaton is already complete.")
        return automaton
    else:
        # Create a copy of the automaton
        new_automaton = automaton
        # Check if the automaton is deterministic
        if not d.is_deterministic(new_automaton):
            print("Automaton is not deterministic.")
            # Determinize the automaton
            new_automaton = d.DeterminizeAutomata(new_automaton)
            # Check if the determinized automaton is complete
            if IsComplete(new_automaton):
                print("Automaton is now complete.")
                return new_automaton
        print("Automaton is (now) deterministic.")
        # Create a copy of the states and add a new state "P"
        new_states = new_automaton.states.copy()
        new_states.append("P")
        # Create a copy of the transitions
        new_transitions = new_automaton.transitions.copy()
        # Ensure every state has a transition for every letter in the alphabet
        for state in new_states:
            for letter in new_automaton.alphabet:
                if (state, letter) not in new_automaton.transitions:
                    new_transitions[(state, letter)] = "P"
        # Return the complete deterministic finite automaton
        return c.Automata(new_states, new_automaton.alphabet, new_transitions, new_automaton.initials, new_automaton.finals, new_automaton.HowManyInitials)
