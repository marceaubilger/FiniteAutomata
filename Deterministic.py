import classAutomata as c

def is_deterministic(automaton):
    """
    @breif : Checks if the given automaton is deterministic.
    @param : An instance of the Automata class.
    @return: True if deterministic, False otherwise.
    """
    if automaton.HaveEpsilonTransitions:
    return False

    # Condition 1: There must be exactly one initial state
    if automaton.HowManyInitials != 1:
        print("There is not one initial state")
        return False

    # Condition 2: No state should have multiple transitions for the same symbol

    for (state, symbol), next_state in automaton.transitions.items():
        if next_state not in automaton.states:
            print("It has more than one end state per transitions")
            return False
    return True

def DeterminizeAutomata(automaton):
    new_transitions = {}
    new_initials = automaton.initials
    howManyInitials = automaton.HowManyInitials
    HadMoreThanOneEntrie = False


    # Case 1: It's an asynchronous automaton
    if automaton.HaveEpsilonTransitions:

        # Expand initial states with epsilon closure
        expanded_initials = set()
        for initial in automaton.initials:
            expanded_initials.update(automaton.EpsilonClosures.get(initial, {initial}))
        new_initials = [
            "".join(sorted(expanded_initials))]  # Create a single new initial state

        unprocessed_states = [new_initials[0]]
        processed_states = set()
        new_states = set(unprocessed_states)

        # While there are unprocessed states, process them
        while unprocessed_states:
            current_state = unprocessed_states.pop(0)
            processed_states.add(current_state)

            # For each symbol in the automaton's alphabet, determine the next state
            for symbol in automaton.alphabet:
                next_state_set = set()

                # For each substate in the current state, look for transitions for the symbol
                for substate in current_state:
                    if (substate, symbol) in automaton.transitions:
                        next_state_set.update(automaton.transitions[(substate, symbol)])

                # Compute the epsilon closure of the next state
                epsilon_closure_set = set()
                for state in next_state_set:
                    epsilon_closure_set.update(automaton.EpsilonClosures.get(state, {state}))
                next_state_set = epsilon_closure_set

                # Convert the next state set into a sorted string for consistency
                new_next_state = "".join(sorted(next_state_set))
                if new_next_state:
                    new_transitions[(current_state, symbol)] = new_next_state

                    # If the next state hasn't been processed or added to unprocessed states, add it
                    if new_next_state not in processed_states and new_next_state not in unprocessed_states:
                        unprocessed_states.append(new_next_state)
                        new_states.add(new_next_state)

        # Find new final states in the determinized automaton
        new_final_states = [state for state in new_states if any(f in state for f in automaton.finals)]

        # Create the new determinized automaton
        new_automaton = c.Automata(list(new_states), automaton.alphabet, new_transitions, new_initials, new_final_states, howManyInitials, False, {})

        #Give the different epsilon-closures :
        print("The ε-closures are :")
        for state, closure in automaton.EpsilonClosures.items():
            print(f"{state} = {sorted(closure)}")


    #Case 2: it's not an asynchronous automaton
    else:
        # If multiple initial states, create a combined new initial state
        if len(automaton.initials) > 1:
            new_initials = ["".join(str(i) for i in automaton.initials)]  # Merge initial states into a string
            howManyInitials = 1

            # Generate transitions for the new initial state NEEDS TO BE MODIFIED TO USE ONLY THE LETTERS USED BY THE JOINT INITIALS STATES AND NOT THE ENTIRE ALPHABET
            for letter in automaton.alphabet:
                next_state = GetNExtState(automaton, new_initials, letter)
                if next_state != "":
                    new_transitions[(new_initials, letter)] = next_state
                    HadMoreThanOneEntrie = True

        # Copy transitions and add missing states if needed
        for (state, symbol), next_state in automaton.transitions.items():
            new_transitions[(state, symbol)] = next_state

            # If the next state is not in automaton.states, add it and create new transitions
            if next_state not in automaton.states:
                automaton.states.append(next_state)

                lettersToUse = FindLetters(automaton, next_state)

                for letter in lettersToUse:  # NEEDS TO BE MODIFIED TO USE ONLY THE LETTERS USED BY THE JOINT STATES AND NOT THE ENTIRE ALPHABET
                    new_transitions[(next_state, letter)] = GetNExtState(automaton, next_state, letter)

        # Remove states that were merged into new_initials from transitions
        if HadMoreThanOneEntrie is True:
            states_to_remove = set(map(str, automaton.initials))  # Convert initial states to strings
            new_transitions = {k: v for k, v in new_transitions.items() if k[0] not in states_to_remove}

        # Find new final states
        new_final_states = [state for state in automaton.states if any(str(f) in str(state) for f in automaton.finals)]

        # Create and return the new automaton
        new_automaton = c.Automata(automaton.states, automaton.alphabet, new_transitions, new_initials, new_final_states, howManyInitials, False, {})
    return new_automaton





def FindLetters(automaton,stateToAnalyse):
    letters=""
    stateToAnalyse=set(stateToAnalyse)
    for s in stateToAnalyse:
        for (state, symbol), next_state in automaton.transitions.items():
            if state==s:
                letters+=symbol
    return letters


def GetNExtState(automaton,stateToAnalyse,symbolToAnalyse):
    listState=list(stateToAnalyse)
    new_next_state=""

    for i in listState:
        for (state, symbol), next_state in automaton.transitions.items():
            if i==state and symbolToAnalyse == symbol:
                new_next_state+=str(next_state).replace("{","").replace("}","").replace(",","").replace(" ","")
    new_next_state_clean=""
    
    #clean the string from duplicates
    for n in new_next_state:
        if n not in new_next_state_clean:
            new_next_state_clean+=n
    return new_next_state_clean
