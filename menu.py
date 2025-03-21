import Reading as r
import Deterministic as d
import classAutomata as c
import Standard as s
import Complete as O
import Complementary as inverse

def getFIleFromInput(val):
    if val<23 and val>0:
        filepath="Automaton"+str(val)
        return  filepath
    
    if val<45 and val>0:
        filepath="Automaton 23 -44/Automaton"+str(val)+".txt"
        return  filepath
    print("Invalid automaton number")
    return 0


def Menu():

    val=int(input("Enter the number of the automaton : \n"))
    filepath=getFIleFromInput(val)
    if filepath!=0:
        automata=r.readFileToDictionary(filepath)
        print(automata)
        DoStuffWithAutomata(automata)


def DoStuffWithAutomata(automata):
    choice=int(input("What would you like to do : \n1 : Enter a new automaton\n2 : Determinize the automaton\n3 : Complete the automaton\n4 : Standardize the automaton\n5 : exit :\n")
    )
    if choice==1:
        Menu()
    if choice==2:
        determinizedAutomata=d.DeterminizeAutomata(automata)
        while d.is_deterministic(determinizedAutomata) != True:
            determinizedAutomata=d.DeterminizeAutomata
        print("Here is the determinized automaton : \n")
        print(determinizedAutomata)
        DoStuffWithAutomata(automata)

    if choice==3:
        complete_automata=O.CompleteAutomata(automata)
        print("Here is the complete automata : \n")
        print(complete_automata)
        DoStuffWithAutomata(automata)
    
    if choice==4:
        if s.isStandard(automata):
            print("The automata is already standard\n")
        else:
            standardizedAutomata=s.Standardize(automata)
            print(standardizedAutomata)
        DoStuffWithAutomata(automata)

    if choice==5:
        exit()
            
    