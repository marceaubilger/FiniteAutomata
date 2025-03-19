class Automata:

    def __init__(self,states,alphabet,transitions,initials,finals,howMany):
        self.alphabet=alphabet              #set of letters
        self.states=states                  #list of states 
        self.initials=initials              #set of initials state
        self.finals=finals                  #set of final state
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
    
    def display(self):
        """
        Display the transition table of the finite automaton.
        This method constructs and prints a formatted transition table that represents the states,
        transitions, and alphabet of the finite automaton. The table includes indicators for initial
        and final states.
        The transition table is printed with the following format:
        - The first row contains the alphabet symbols.
        - Each subsequent row represents a state and its transitions for each symbol in the alphabet.
        - Initial states are marked with '→'.
        - Final states are marked with '←'.
        - States that are both initial and final are marked with '↔'.
        The table is formatted to align the state names and transition values based on the maximum length
        of the state names and transition values (still untested for a wide range of automaton).
        Returns:
            None
        Notes :
        - This method is not yet guaranteed to format for a wide range of automaton.
        """
        
        # Initialize a list of lists where each sublist contains a single state
        stats = [[state] for state in self.states]
        
        # Determine the maximum length of state names and transition values for formatting
        length = max([len(state) for state in self.states + [val for val in self.transitions.values()]])
        print("length",length)
        length += length % 2  # Ensure the length is even
        print("length even",length)
        # Initialize the transition table with the alphabet symbols, formatted to the determined length
        trans = [[' '*5]]
        for letter in self.alphabet:
            spaces = ' ' * (length//2 - len(letter) + 1)  # Create a string of spaces for formatting
            trans[0].append(spaces[1:] + letter + spaces)  # Append the formatted alphabet symbol
        print(trans[0])
        
        # Iterate over each state to construct the rows of the transition table
        for i in range(len(stats)):
            # Check if the current state is both an initial and final state
            if stats[i][0] in self.finals and stats[i][0] in self.initials:
                line = ['↔', stats[i][0]]  # Mark with '↔' if both initial and final
            # Check if the current state is a final state
            elif stats[i][0] in self.finals:
                line = ['←', stats[i][0]]  # Mark with '←' if final
            # Check if the current state is an initial state
            elif stats[i][0] in self.initials:
                line = ['→', stats[i][0]]  # Mark with '→' if initial
            # If the state is neither initial nor final
            else:
                line = [' ', stats[i][0]]  # No special marker
            for letter in self.alphabet:  # Iterate over each symbol in the alphabet
                if (stats[i][0], letter) in self.transitions:  # Check if a transition exists for the state-symbol pair
                    new_trans = self.transitions[(stats[i][0], letter)]  # Get the resulting state for the transition
                    line.append(' ' * (length//2 - len(new_trans)) + new_trans + ' ' * (length//2 - len(new_trans)+1) )  # Append the formatted resulting state
                else:
                    line.append(' ' * length)  # Append an empty cell if no transition exists
            trans.append(line)  # Add the constructed row to the transition table
        
        # Print the transition table with '|' as the column separator and each row on a new line
        print(str(trans).replace("],", "\n").replace(",", "|").replace("'", "").replace("[", "").replace("]", ""))