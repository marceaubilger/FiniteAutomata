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
        Displays the finite automaton's transition table in a formatted manner.

        The method constructs a table where each row represents a state and each column represents a symbol from the alphabet.
        The table shows the resulting state for each state-symbol pair based on the transitions defined in the automaton.

        The table is printed with the following format:
        - The first row contains the alphabet symbols.
        - Each subsequent row starts with a state and contains the resulting states for each symbol in the alphabet.
        - Empty cells indicate no transition for the corresponding state-symbol pair.

        Example output:
        |  | a| b|
        |q0|q1|  |
        |q1|  |q2|
        |q2|q0|q1|

        Notes: 
        - The table is printed with '|' as the column separator and each row on a new line.
        - The method makes an attempt at aligning the columns, but the output may not be perfectly aligned.
        """
        # Initialize a list of lists where each sublist contains a single state
        stats = [[state] for state in self.states]
        
        # Create a list with a space followed by the alphabet symbols
        alpha = [' '] + self.alphabet
        
        # Determine the maximum length of state names and transition values for formatting
        length = max([len(state) for state in self.states + [val for val in self.transitions.values()]])
        
        # Initialize the transition table with the alphabet symbols, formatted to the determined length
        trans = [[' ' * (length - len(letter)) + letter for letter in alpha]]
        
        # Iterate over each state to construct the rows of the transition table
        for i in range(len(stats)):
            line = [stats[i][0]]  # Start the row with the current state
            for letter in alpha[1:]:  # Iterate over each symbol in the alphabet
                if (stats[i][0], letter) in self.transitions:  # Check if a transition exists for the state-symbol pair
                    new_trans = self.transitions[(stats[i][0], letter)]  # Get the resulting state for the transition
                    line.append(' ' * (length - len(new_trans)) + new_trans)  # Append the formatted resulting state
                else:
                    line.append(' ' * length)  # Append an empty cell if no transition exists
            trans.append(line)  # Add the constructed row to the transition table
        
        # Print the transition table with '|' as the column separator and each row on a new line
        print(str(trans).replace("],", "\n").replace(",", "|").replace("'", "").replace("[", "").replace("]", ""))