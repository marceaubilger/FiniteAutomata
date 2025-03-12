def build_matrix_from_Automata(content):
    """
    @breif : function to build the base matrix of an automaton based on the file input
    @param : the content of the file from read_automata_from_file
    @return : the automata matrix
    """
    transitions=content[5].split(" ")
    alphabet=list(content[1])
    matrix_width=len(content[1])
    matrix_lenght=int(content[2])
    matrix_automata=[]

    for i in range(0,matrix_lenght):#build the matrix by putting / in every spots
        matrix_row=[]
        for j in range (0,matrix_width):
            matrix_row.append("/")
        matrix_automata.append(matrix_row)

    for k in range(0,len(transitions)):#replace the default / by the correct transitions when a transition is there
        tmp_tran=transitions[k].split()
        if matrix_automata[int(tmp_tran[0][0])][alphabet.index(tmp_tran[0][1])]=="/": #check if the spot was taken by a / -> replace it
            matrix_automata[int(tmp_tran[0][0])][alphabet.index(tmp_tran[0][1])]=tmp_tran[0][2]
        else: #if a value is in the spot append the next transition to it 
            matrix_automata[int(tmp_tran[0][0])][alphabet.index(tmp_tran[0][1])]=matrix_automata[int(tmp_tran[0][0])][alphabet.index(tmp_tran[0][1])]+","+tmp_tran[0][2]
    
    return matrix_automata




def Print_Matrix(matrix): 
    """
    @brief : simple function to print a matrix more elegantly
    @param : the matrix to print
    @return : nothing
    """
    for row in matrix:
        print(" ".join(map(str, row)))