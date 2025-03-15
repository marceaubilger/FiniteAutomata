import classAutomata as c
def readFileToDictionnary(file_name):
    """
    @breif : read the automa from a text file
    @param : the file name
    @return : the text
    """
    with open(file_name,"r",encoding="utf-8") as file:
        text=file.readlines()
    return text

def CreateAutomata(text):
    
    alphabet=list(text[1].strip())
    
    states =["."]*int(text[2].strip())
    for s in range(0,int(text[2].strip())):
        states[s]=str(s)

    tmp_initials=text[3].split(" ")
    HowManyInitials=len(tmp_initials)
    initials = list(int(k) for k in tmp_initials)

    tmp_finals=(text[4].strip()).split(" ")
    finals = list(m for m in tmp_finals)

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
    
    automata=c.Automata(states,alphabet,transition_dict,initials,finals,HowManyInitials)
    return automata