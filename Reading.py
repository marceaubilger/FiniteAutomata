
def read_Automata_From_File(file_name):
    with open(file_name,"r",encoding="utf-8") as file:
        text=file.readlines()
    return text

def build_matrix_from_Automata(content):
    """
    @breif : function to build the base matrix of an automaton based on the file input
    @param : the content of the file from read_automata_from_file
    @return : the automata matrix
    """
    transitions=content[5].split(" ")
    entries_exit=content[3].split(" ")
    alphabet=list(content[1])
    matrix_width=len(content[1])+2
    matrix_lenght=int(content[2])
    matrix_automata=[]

    for i in range(0,matrix_lenght):#build the matrix by putting / in every spots
        matrix_row=[]
        for j in range (1,matrix_width+2):
            matrix_row.append("/")
        matrix_row[0]='-'
        matrix_automata.append(matrix_row)

    for m in range(0,len(entries_exit)): #adds the type of entries matching the states
        tmp_tran=entries_exit[m].split()
        matrix_automata[int(tmp_tran[0][0])][0]=tmp_tran[0][1]
    

    for p in range (0,int(content[2])): #adds the states
        matrix_automata[p][1]=p


    for k in range(0,len(transitions)):#replace the default / by the correct transitions when a transition is there
        tmp_tran=transitions[k].split()
        if matrix_automata[int(tmp_tran[0][0])][alphabet.index(tmp_tran[0][1])+2]=="/": #check if the spot was taken by a / -> replace it
            matrix_automata[int(tmp_tran[0][0])][alphabet.index(tmp_tran[0][1])+2]=tmp_tran[0][2]
        else: #if a value is in the spot append the next transition to it 
            matrix_automata[int(tmp_tran[0][0])][alphabet.index(tmp_tran[0][1])+2]+=","+tmp_tran[0][2]
        
    
    return matrix_automata




def Print_Matrix(matrix): 
    """
    @brief : Simple function to print a matrix with aligned columns.
    @param matrix: The matrix to print (list of lists).
    @return: Nothing.
    """
    # Determine the maximum width of each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*matrix)]

    # Print the matrix with formatted columns
    for row in matrix:
        print("    ".join(f"{str(item):<{w}}" for item, w in zip(row, col_widths)))
