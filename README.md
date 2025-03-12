# FiniteAutomata

Bienvenue dans ce projet visant à automatiser les calculs sur automates. Pour { raison rapide } nous utiliserons le language { nom du language } et { particularité du code (gestion de mémoire, POO, ...)}. 

Dans le code un FA est representé de cette manière :

class FA():
    def __init__(self):
    
      self.states={state:"E" or state : " " or state : "S" or state:"T"} // with E for entry, S for Exit, T for two (entry and exit) and " " for none
    
      self.letters=[letter 1, letter 2,..., letter n]
      
      self.automaton=[[state, next state for letter 1, next state for letter 2,....,next state for letter n]]
      
      self.det=0
      
      self.stand=0
