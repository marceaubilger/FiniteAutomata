import Deterministic as d
class Automata:

    def __init__(self,states,alphabet,transitions,initials,finals,howMany):
        self.alphabet=alphabet              #list of letters
        self.states=states                  #list of states 
        self.initials=initials              #list of initials state
        self.finals=finals                  #list of final state
        self.transitions=transitions        #dictionnary of transitions
        self.HowManyInitials=howMany        #number of initials states    
    
    def __str__(self):
     return (f"Alphabet: {self.alphabet}\n"
            f"States: {self.states}\n"
            f"Initial States: {self.initials}\n"
            f"Final States: {self.finals}\n"
            f"How many Initials: {self.HowManyInitials}\n"
            f"Transitions:\n" +
            "\n".join([f"  ({k[0]}, '{k[1]}') → {v}" for k, v in self.transitions.items()]))
    
def ReadWord(automata,word):
   if d.is_deterministic(automata)==True:
        q=automata.initials
        while word!="":
            try :
                q=automata.transitions[(q[0],word[0])]
                word=word[1:]
            except KeyError:
                return False

        
        if q in automata.finals:
           return True
        return False