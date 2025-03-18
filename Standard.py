import classAutomata as c

def isStandard(automata):
    return len(automata.initials) == 1

def standardize(automata):
    if isStandard(automata):
        return automata
    else:
        newInitial = "I"
        newTransitions = {}
        for (startState,letter), endState in automata.transitions.items():
            if startState == automata.initials:
                newTransitions[(newInitial, letter[1])] = endState
        return c.Automata(automata.states, automata.alphabet, automata.transitions+newTransitions, [newInitial], automata.finals, 1)