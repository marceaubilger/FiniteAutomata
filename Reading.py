import classAutomata as c
def readFileToDictionnary(file_name):
    """
    @breif : read the automa from a text file and make it into a class
    @param : the file name
    @return : the Automata class filled with the automaton infos
    """
    with open(file_name,"r",encoding="utf-8") as file:
        text=file.readlines()
    
    alphabet=set(text[1].strip())
    
    states = set(range(int(text[2].strip())))

    tmp_initials=text[3].split(" ")
    initials = set(int(k) for k in tmp_initials)

    tmp_finals=text[4].split(" ")
    finals = set(int(m) for m in tmp_finals)

    transitions = text[5].split()  # Split by spaces
    print(transitions)
    transition_dict = {}

    for transition in transitions:
        state, symbol, next_state = transition[0], transition[1], transition[2]  # Extract elements
        state, next_state = int(state), int(next_state)

        if (state, symbol) in transition_dict:
            transition_dict[(state, symbol)].add(next_state)  # Add to existing set
        else:
            transition_dict[(state, symbol)] = {next_state}  # Create new set
    
    automata=c.Automata(states,alphabet,transition_dict,initials,finals)
    return automata