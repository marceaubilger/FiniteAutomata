import Reading as r
import Deterministic as d
import classAutomata as c
import Standard as s



text=r.readFileToDictionary("TestAutomata")

automata=r.CreateAutomata(text)

print(automata)
print("\n")

new_automaton=s.Standardize(automata)
print(new_automaton)

# new_automaton=d.DeterminizeAutomata(automata)
# print(new_automaton)
# print("1\n")

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
# print(d.is_deterministic(new_automaton))
print(new_automaton.transitions)
print(s.isStandard(new_automaton))