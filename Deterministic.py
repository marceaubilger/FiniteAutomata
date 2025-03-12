import Reading as r

def Is_Deterministic(matrix_automaton):
    """
    @brief : check is a given automaton is deterministic
    @param : the matrix of the automaton
    @return : True or False
    """

    count_entries=0
    for i in matrix_automaton:#check for more than one entrie
        if 'T' in matrix_automaton:
            count_entries+=1
    if count_entries>1: return False

    for row in matrix_automaton:
        if ',' in row: return False
    
    return True


def Is_Complete(matrix_automaton):
    """
    @brief : check is a given automaton is complete
    @param : the matrix of the automaton
    @return : True or False
    """
    for row in matrix_automaton:
        if "/" in row: return False
    return True


def Check_For_Existing_State(matrix_automaton,state):
    """
    @breif : check in the automaton matrix if a given state already exist
    @param 1 : the automaton matrix
    @param 2 : the state to look for
    @return : True or False
    """

    for row in matrix_automaton:
        if matrix_automaton[row][1]==state:
            return True

def Check_For_Entries_Exits(matrix_automaton,states):
    """
    @breif : gives the entries ans or exits associated to a state either singular or made of many states
    @param1 : the automaton matrix
    @param2 : the states whose entries and exit we look for
    @return : the list of entries and exits
    """
    entries_exits=[]
    state=states.split()
    for i in state:
        if matrix_automaton[int(i)][0]!='-': entries_exits.append(matrix_automaton[int(i)][0])
    return entries_exits


#def Determinisation(matrix_automaton):

