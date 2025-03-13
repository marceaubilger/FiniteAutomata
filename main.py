import Reading as r
import Deterministic as d
import classAutomata as c



automata=r.readFileToDictionnary("TestAutomata")
print(automata)

print(d.is_deterministic(automata))

print(d.IsComplete(automata))
