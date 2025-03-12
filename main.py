import Reading as r
import Deterministic as d


matrix=r.build_matrix_from_Automata(r.read_Automata_From_File("TestAutomata"))
r.Print_Matrix(matrix)


print(d.Is_Deterministic(matrix))
print(d.Is_Complete(matrix))
print(d.Check_For_Entries_Exits(matrix,str(4)))