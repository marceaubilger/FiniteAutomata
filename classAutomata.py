class Automata:

    def __init__(self,states,alphabet,transitions,initials,finals):
        self.alphabet=alphabet              #set of letters
        self.states=states                  #set of states 
        self.initials=initials              #set of initials state
        self.finals=finals                  #set of final state
        self.transitions=transitions        #dictionnary of trnasitions
    
    
    def __str__(self):
     return (f"Alphabet: {self.alphabet}\n"
            f"States: {self.states}\n"
            f"Initial States: {self.initials}\n"
            f"Final States: {self.finals}\n"
            f"Transitions:\n" +
            "\n".join([f"  ({k[0]}, '{k[1]}') → {v}" for k, v in self.transitions.items()]))
    
