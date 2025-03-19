import Reading as r
import Deterministic as d
import classAutomata as c
import Standard as s
import Complete as O
import Complementary as inverse


text=r.readFileToDictionary("TestAutomata")

print("Initial automaton : \n")

automata=r.CreateAutomata(text)

print(automata)
print("\n")

automata.display()
# 
# print("\nDeterminizing the automaton : \n")
# 
# d_automaton=d.DeterminizeAutomata(automata)
# print(d_automaton)
# 
# 
# if d.is_deterministic(new_automaton) ==False:
#     new_automaton=d.DeterminizeAutomata(new_automaton)
#     print(new_automaton)
#     print("2\n")
# if d.is_deterministic(new_automaton) ==False:
#     new_automaton=d.DeterminizeAutomata(new_automaton)
#     print(new_automaton)
#     print("3\n")

# print(d.is_deterministic(new_automaton))

# t=0
# while d.is_deterministic(new_automaton)==False and t<500:
#     new_automaton=d.DeterminizeAutomata(new_automaton)
#     t+=1
#     print(t)
# print(d.is_deterministic(d_automaton))
# 
# print("\nStandardizing the automaton : \n")
# s_automaton=s.Standardize(automata)
# print(s_automaton)
# print(s_automaton.transitions)
# print(s.isStandard(s_automaton))
# 
# print("\nCompleting the automaton : \n")
# c_automaton=O.CompleteAutomata(automata)
# print(c_automaton)
# print(O.IsComplete(c_automaton))
# 
# 
# print("\nComplementing the automaton : \n")
# complement=inverse.Complementary(automata)
# print(complement)