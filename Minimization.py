import classAutomata as c
import Complete as O

"""When I wrote this code, only God and I understood what I was doing.
Now, God only knows."""

#def MinimizeAutomata(automata):
#    automata=O.CompleteAutomata(automata)
#    states=automata.states
#    final_states=automata.finals
#    transitions=automata.transitions
#    alphabet=automata.alphabet
#    new_final_states=[]
#    tmp_states=states.copy()
#    new_transitions={}
#    #Eliminate common sense options
#    if (len(states)==1 and 'P' not in states) or (len(states)==2 and 'P' in states):
#        print("nope")
#        return automata
#
#    #Eliminate unreachable states
#    for state in states:
#        if state not in transitions.values() and state not in automata.initials:
#            tmp_states.remove(state)
#    
#    previous_transitions=transitions
#    iteration = 0
#    while previous_transitions != new_transitions:
#        print(f"Iteration {iteration}:")
#        print(f"Previous Transitions: {previous_transitions}")
#        print(f"New Transitions: {new_transitions}")
#        previous_transitions = new_transitions.copy()
#        new_transitions={}
#        GroupNT={}
#        GroupT={}
#        for (state, letter), destination in transitions.items():
#            print(f"State: {state}, Letter: {letter}, Destination: {destination}")
#            if state in tmp_states:
#                if state not in final_states:
#                    GroupNT[(state,letter)]=destination in final_states
#                else:
#                    new_final_states.append(state)
#                    GroupT[(state,letter)]=destination in final_states
#        print(f"GroupNT: {GroupNT}")
#        print(f"GroupT: {GroupT}")
#        for (state,letter), terminot1 in GroupNT.items():
#            for (state2,letter2), terminot2 in GroupNT.items():
#                if state!=state2:
#                    tmp_dest1=[]
#                    tmp_dest2=[]
#                    for letter in alphabet:
#                        tmp_dest1.append(terminot1)
#                        tmp_dest2.append(terminot2)
#                    if tmp_dest1==tmp_dest2:
#                        new_state=state+state2
#                        for letter in alphabet:
#                            if (state, letter) in transitions:
#                                new_transitions[(new_state,letter)]=transitions[(state,letter)]
#        for (state,letter), terminot1 in GroupT.items():
#            for (state2,letter2), terminot2 in GroupT.items():
#                if state!=state2:
#                    tmp_dest1=[]
#                    tmp_dest2=[]
#                    for letter in alphabet:
#                        tmp_dest1.append(terminot1)
#                        tmp_dest2.append(terminot2)
#                    if tmp_dest1==tmp_dest2:
#                        new_state=state+state2
#                        for letter in alphabet:
#                            if (state, letter) in transitions:
#                                new_transitions[(new_state,letter)]=transitions[(state,letter)]
#                        if state in tmp_states:
#                            tmp_states.remove(state)
#                        if state2 in tmp_states:
#                            tmp_states.remove(state2)
#                        if new_state not in tmp_states or state2+state not in tmp_states:
#                            tmp_states.append(new_state)
#                        new_final_states.pop(new_final_states.index(state))
#                        new_final_states.pop(new_final_states.index(state2))
#                        new_final_states.append(new_state)
#        print(f"New States: {tmp_states}")
#        print(f"New Final States: {new_final_states}")
#        iteration += 1
#    return c.Automata(tmp_states,alphabet,new_transitions,automata.initials,new_final_states,automata.HowManyInitials)