import Reading as r
import Deterministic as d
import classAutomata as c
import Standard as s
import Complete as O
import Complementary as inverse
import menu as m
import os


# text=r.readFileToDictionary("Automaton 23 -44/Automaton31.txt")

# print("Initial automaton : \n")

# automata=r.CreateAutomata(text)

# print(automata)

# print("\nDeterminizing the automaton : \n")

# d_automaton=d.DeterminizeAutomata(automata)
# print(d_automaton)


# print(d.is_deterministic(d_automaton))

# print("\nStandardizing the automaton : \n")
# s_automaton=s.Standardize(automata)
# print(s_automaton)
# print(s_automaton.transitions)
# print(s.isStandard(s_automaton))

# print("\nCompleting the automaton : \n")
# c_automaton=O.CompleteAutomata(automata)
# print(c_automaton)
# print(O.IsComplete(c_automaton))


# print("\nComplementing the automaton : \n")
# complement=inverse.Complementary(automata)
# print(complement)


m.Menu()