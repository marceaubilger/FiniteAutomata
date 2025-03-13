import Reading as r
from itertools import chain

def Is_Deterministic(matrix_automaton):
    """
    @brief : check is a given automaton is deterministic
    @param : the matrix of the automaton
    @return : True or False
    """

    count_entries=0
    for i in matrix_automaton:#check for more than one entrie
        if 'T' in i:
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


def Check_For_Existing_Value(matrix_automaton, value):
    """
    @brief : Check if a given value already exists in the second column of the automaton matrix.
    @param 1 : matrix_automaton - The automaton matrix.
    @param 2 : value - The value to look for.
    @return : True if found, False otherwise.
    """
    for i in range(0,len(matrix_automaton)):
        if str(value)==str(matrix_automaton[i][1]): return True
    return False


def Check_For_Entries_Exits(matrix_automaton,states):
    """
    @breif : gives the entries ans or exits associated to a state either singular or made of many states
    @param1 : the automaton matrix
    @param2 : the states whose entries and exit we look for
    @return : the list of entries and exits
    """
    entries_exits=[]
    state_list = list(states)
    for i in state_list:
        if matrix_automaton[int(i)][0]!='-': entries_exits.append(matrix_automaton[int(i)][0])
    return entries_exits

def Join_two_states(matrix_automaton,state):

    joint_states=["/"]*len(matrix_automaton[0])
    state=list(state)
    
    for i in state:
        p=2
        i=int(i)
        for j in range(0,len(matrix_automaton)):
            if i==matrix_automaton[j][1]:
                joint_states[p]+=str(i)
                p+=1



    for k in range(0,len(joint_states)):
        if joint_states[k]!="/":
            joint_states[k]=joint_states[k].replace("/","")
    return joint_states


# def Determinisation(matrix_automaton):
#     new_row_for_state=["/"]*len(matrix_automaton[0])

#     for i in range(0,len(matrix_automaton)):
#         for col in range(2,len(matrix_automaton[0])):


#             #handles the new states by adding them to the matrix
#             if matrix_automaton[i][col]!='/' and Check_For_Existing_Value(matrix_automaton,matrix_automaton[i][col]) == False:
#                 new_row_for_state[1]=matrix_automaton[i][col]
#                 if 'F' in Check_For_Entries_Exits(matrix_automaton,matrix_automaton[i][col]):
#                     new_row_for_state[0]='F'
#                 tmp_new_row=Join_two_states(matrix_automaton,matrix_automaton[i][col])
#                 for j in range(2,len(matrix_automaton[0])):
#                     new_row_for_state[j]=tmp_new_row[j]
                

                


#     if new_row_for_state[0]=='/': new_row_for_state[0]=new_row_for_state[0].replace("/","-")
#     matrix_automaton.append(new_row_for_state)
#     return matrix_automaton




def determinize_automaton(matrix, alphabet):
    """
    @brief : Converts a non-deterministic automaton to a deterministic one.
    @param matrix: The automaton matrix (list of lists).
    @param alphabet: The alphabet used in the automaton.
    @return: The determinized automaton matrix.
    """
    new_matrix = []
    state_map = {}  # Maps new state representations to their indices in new_matrix
    queue = []  # Queue to process new states

    # Get the initial state(s)
    initial_states = {i for i, row in enumerate(matrix) if 'T' in row[0]}
    queue.append(frozenset(initial_states))  # Start from the initial states as a set
    state_map[frozenset(initial_states)] = 0

    while queue:
        current_set = queue.pop(0)  # Process a new state (set of original states)
        row = ['-'] * (len(alphabet) + 2)
        row[0] = 'T' if any(matrix[s][0] == 'T' for s in current_set) else ('F' if any(matrix[s][0] == 'F' for s in current_set) else '-')
        row[1] = len(new_matrix)  # Assign a unique index for this new state

        # Compute transitions
        for j, symbol in enumerate(alphabet, start=2):
            next_states = set(chain.from_iterable(
                matrix[s][j] if matrix[s][j] != '/' else [] for s in current_set
            ))

            if next_states:
                next_state_set = frozenset(map(int, next_states))
                if next_state_set not in state_map:
                    state_map[next_state_set] = len(new_matrix) + len(queue)
                    queue.append(next_state_set)

                row[j] = state_map[next_state_set]
            else:
                row[j] = '/'

        new_matrix.append(row)

    return new_matrix