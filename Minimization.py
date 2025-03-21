import classAutomata as c
import Complete as O

def MinimizeAutomata(automata):
    print("Not implemented yet")
    return automata
"""    automata=O.CompleteAutomata(automata)
    states=automata.states
    final_states=automata.final_states
    transitions=automata.transitions
    alphabet=automata.alphabet
    tmp_non_final_states=[]
    tmp_states=states
    GroupNT={}
    GroupT={}
    for (state, letter), destination in transitions:
        if state not in final_states:
            tmp_non_final_states.append(state)
            GroupNT[(state,letter)]=destination in final_states
        else:
            GroupT[(state,letter)]=destination in final_states
            """