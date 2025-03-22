import Reading as r
import Deterministic as d
import classAutomata as c
import Standard as s
import Complete as O
import Complementary as inverse

def getFIleFromInput(val):
    if val>=1 and val<=44:
        filepath="Automaton/Automaton"+str(val)+".txt"
        return  filepath
    print("Invalid automaton number")
    return 0

def choseAutomaton():
    val=input("Enter the number of the automaton : ")
    while not val.isdigit() or int(val)<1 or int(val)>44:
        print("Invalid input, please enter an integer between 1 and 44")
        val=input("Enter the number of the automaton : ")
    val=int(val)
    return val

def choseOption():
    choice=input("What would you like to do ? \n  1 : Enter a new automaton\n  2 : Determinize the automaton\n  3 : Complete the automaton\n  4 : Standardize the automaton\n  5 : Print out the complementary\n  6 : Read a word\n  7 : exit \n")
    while not choice.isdigit() or choice<"1" or choice>"7" or len (choice)!=1:
        print("Invalid input, please enter an integer between 1 and 7")
        choice=input("What would you like to do ? \n  1 : Enter a new automaton\n  2 : Determinize the automaton\n  3 : Complete the automaton\n  4 : Standardize the automaton\n  5 : Print out the complementary\n  6 : Read a word\n  7 : exit \n")
    choice=int(choice)
    return choice

def Menu():
    val=choseAutomaton()
    filepath=getFIleFromInput(val)
    if filepath!=0:
        automata=r.readFileToDictionary(filepath)
        automata= r.CreateAutomata(automata)
        print(str(automata))
        DoStuffWithAutomata(automata)


def DoStuffWithAutomata(automata):
    choice=choseOption()
    while not(choice<1 or choice>6):
        if choice==1:
            val=choseAutomaton()
            filepath=getFIleFromInput(val)
            if filepath!=0:
                automata=r.readFileToDictionary(filepath)
                automata= r.CreateAutomata(automata)
                automata.display()
        if choice==2:
            if d.is_deterministic(automata):
                print("The automata is already deterministic")
            else:
                determinizedAutomata=d.DeterminizeAutomata(automata)
                while d.is_deterministic(determinizedAutomata) != True:
                    determinizedAutomata=d.DeterminizeAutomata(determinizedAutomata)
                print("Here is the determinized automaton : \n")
                determinizedAutomata.display()

        if choice==3:
            if O.IsComplete(automata):
                print("The automata is already complete\n")
            else: 
                complete_automata=O.CompleteAutomata(automata)
                print("Here is the complete automata : \n")
                complete_automata.display()

        if choice==4:
            if s.isStandard(automata):
                print("The automata is already standard\n")
            else:
                standardizedAutomata=s.Standardize(automata)
                print("Here is the standardized automata : \n")
                standardizedAutomata.display()
        
        if choice==5:
            complementaryAutomata=inverse.Complementary(automata)
            print("Here is the complementary automata : \n")
            complementaryAutomata.display()
        
        if choice==6:
            word=input("Enter the word to try : ")
            if c.ReadWord(automata,word)==True:
                print("The word is recognized \n")
            else:
                print("The word is not recognized\n")
        
        choice=choseOption()
    if choice==7:
        print("Goodbye")
    