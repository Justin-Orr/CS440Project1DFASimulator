import sys


# Tanner Dyer - A20437354
# Justin Orr - A20374635
# Safa Slote - A20420223


class DFA:
    def __init__(self, number_of_states, number_of_accepting_states, accepting_states, 
                num_of_alphabet_chars, alphabet_chars, num_of_transitions, transitions, dfa_input):
                self.number_of_states = number_of_states
                self.number_of_accepting_states = number_of_accepting_states
                self.accepting_states = accepting_states
                self.num_of_alphatbet_chars = num_of_alphabet_chars
                self.alphabet_chars = alphabet_chars
                self.num_of_transitions = num_of_transitions
                self.transitions = transitions
                self.dfa_input = dfa_input


    def simulateDFA(self):
        s = 0
        c = self.dfa_input[0]
        
        for i in range(0, len(self.dfa_input)):
            print(s, c, end=' ')
            c = self.dfa_input[i]
            s = self.transition(s, c)
            if s == -1:
                print("\nExecution cannot proceed:\n    Current symbol: {}".format(c))
                break
        
        print()

        if str(s) in self.accepting_states:
            print("Yes")
        else:
            print("No")

    # c being equal to a space character is the same as an empty string in our transition table
    # based on the project description. Therefore in order to handle c for this case, we must 
    # compare to see if it is equal to a space character and simultaneously see if the character 
    # in the transition function is equal to empty string
    def transition(self, s, c):
        for t in self.transitions:
            new_t = t.replace(' ', '').split(',')
            if int(new_t[0]) == s:
                if new_t[1] == c:
                    return int(new_t[2])
                elif c == ' ' and new_t[1] == '':
                    return int(new_t[2])
        return -1

# generates a DFA object from an input file
def generateDFA(filename):
    file = open(filename, 'r')

    lines = file.readlines()

    # get transition functions
    num_transitions = int(lines[5])
    transitions = []
    for i in range(6, 6 + num_transitions):
        transitions.append(lines[i].replace("\n", ""))

    dfa = DFA(
        int(lines[0].rstrip()), # number of states
        int(lines[1].rstrip()), # number of accepting states
        lines[2].rstrip(),      # list of accepting states
        int(lines[3].rstrip()), # number of chars in alphabet
        lines[4].replace("\n", ""), # chars in alphabet
        int(num_transitions),       # number of transitions
        transitions,                # transition functions
        lines[6 + num_transitions].rstrip() # dfa input
    )

    return dfa

if __name__ == "__main__":
    dfa = generateDFA(sys.argv[1])
    dfa.simulateDFA()
