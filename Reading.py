import classAutomata as c
def readFileToDictionary(file_name):
    """
    @breif : read the automa from a text file
    @param : the file name
    @return : every line of the file in a list
    """
    with open(file_name,"r",encoding="utf-8") as file:
        text=file.readlines()
    return text

def CreateAutomata(text):
    
    alphabet=list(text[1].strip())
    closures = {}

    if alphabet[-1] == "ε":
        EpsilonTransitions = True
        alphabet.pop(-1)
    else:
        EpsilonTransitions = False
    
    states =["."]*int(text[2].strip())
    for s in range(0,int(text[2].strip())):
        states[s]=str(s)

    tmp_initials=text[3].split(" ")
    HowManyInitials=len(tmp_initials)
    initials = [k[:-1] if k[-1] == "\n" else k for k in tmp_initials]
    
    tmp_finals=text[4].split(" ")
    finals = [k[:-1] if k[-1] == "\n" else k for k in tmp_finals]

    transitions = text[5].split()  # Split by spaces
    transition_dict = {}

    for transition in transitions:
        transition=transition.split(",")
        state, symbol, next_state = transition[0], transition[1], transition[2]  # Extract elements
        #state, next_state = int(state), int(next_state)

        if (state, symbol) in transition_dict:
            transition_dict[(state, symbol)]+=next_state  # Add to existing set
        else:
            transition_dict[(state, symbol)] = next_state  # Create new set

    if EpsilonTransitions:
        closures = epsilon_closure_all(states, transition_dict)
    
    automata = c.Automata(states, alphabet, transition_dict, initials, finals, HowManyInitials, EpsilonTransitions, closures)
    return automata


# Find the epsilon closure of a State
def epsilon_closure(state, transition_dict):
    """Compute the epsilon-closure of a given state in the automaton."""
    closure = set()  # Set to store the closure
    stack = [state]  # Stack for DFS traversal

    while stack:
        current_state = stack.pop()
        if current_state not in closure:
            closure.add(current_state)
            # Check for epsilon (ε) transitions
            if (current_state, "ε") in transition_dict:
                for next_state in transition_dict[(current_state, "ε")]:
                    stack.append(next_state)

    return closure


# Find all epsilon closures of the automata
def epsilon_closure_all(states, transition_dict):
    """Compute the epsilon-closure for all states in the automaton."""
    return {state: epsilon_closure(state, transition_dict) for state in states}
