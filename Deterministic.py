import classAutomata as c

def is_deterministic(automaton):
    """
    @breif : Checks if the given automaton is deterministic.
    @param : An instance of the Automata class.
    @return: True if deterministic, False otherwise.
    """

    # Condition 1: There must be exactly one initial state
    if automaton.HowManyInitials != 1:
        print("not one state")
        return False

    # Condition 2: No state should have multiple transitions for the same symbol

    for (state, symbol), next_state in automaton.transitions.items():
        if next_state not in automaton.states:
            print("its because transitions")
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

def DeterminizeAutomata(automaton):
    new_transitions = {}
    new_initials = automaton.initials
    howManyInitials=automaton.HowManyInitials
    HadMoreThanOneEntrie=False

    # If multiple initial states, create a combined new initial state
    if len(automaton.initials) > 1:
        new_initials = ["".join(str(i) for i in automaton.initials)]  # Merge initial states into a string
        howManyInitials=1
        
        # Generate transitions for the new initial state NEEDS TO BE MODIFIED TO USE ONLY THE LETTERS USED BY THE JOINT INITIALS STATES AND NOT THE ENTIRE ALPHABET
        for letter in automaton.alphabet:
            next_state = GetNExtState(automaton, new_initials, letter)
            if next_state!="":
                new_transitions[(new_initials, letter)] = next_state
                HadMoreThanOneEntrie=True

    # Copy transitions and add missing states if needed
    for (state, symbol), next_state in automaton.transitions.items():
        new_transitions[(state, symbol)] = next_state

        # If the next state is not in automaton.states, add it and create new transitions
        if next_state not in automaton.states:
            automaton.states.append(next_state)

            lettersToUse=FindLetters(automaton,next_state)

            for letter in lettersToUse:#NEEDS TO BE MODIFIED TO USE ONLY THE LETTERS USED BY THE JOINT STATES AND NOT THE ENTIRE ALPHABET
                new_transitions[(next_state, letter)] = GetNExtState(automaton, next_state, letter)

    # Find new final states
    new_final_states = [state for state in automaton.states if any(str(f) in str(state) for f in automaton.finals)]

    # Remove states that were merged into new_initials from transitions
    if HadMoreThanOneEntrie is True:
        states_to_remove = set(map(str, automaton.initials))  # Convert initial states to strings
        new_transitions = {k: v for k, v in new_transitions.items() if k[0] not in states_to_remove}

    # Create and return the new automaton
    new_automaton = c.Automata(automaton.states, automaton.alphabet, new_transitions, new_initials, new_final_states,howManyInitials)
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