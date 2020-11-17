import sys


# Tanner Dyer - A20437354
# Justin Orr - A20374635
# Safa Slote - A20420223


class NFA:
    def __init__(self, number_of_states, number_of_accepting_states, accepting_states, 
                num_of_alphabet_chars, alphabet_chars, num_of_transitions, transitions, 
                num_null_transitions, null_transitions, nfa_input):
                self.number_of_states = number_of_states
                self.number_of_accepting_states = number_of_accepting_states
                self.accepting_states = accepting_states
                self.num_of_alphatbet_chars = num_of_alphabet_chars
                self.alphabet_chars = alphabet_chars
                self.num_of_transitions = num_of_transitions
                self.transitions = transitions
                self.num_null_transitions = num_null_transitions
                self.null_transitions = null_transitions
                self.nfa_input = nfa_input


    def epsilonClosure(self, state):
        end_states = []
        for null_transition in self.null_transitions:
            if null_transition[0] == state:
                end_states.append(null_transition[-1])
        return end_states


    def simulateNFA(self):
        s = 0
        c = self.nfa_input[0]
        
        for i in range(0, len(self.nfa_input)):
            print(s, c, end=' ')
            c = self.nfa_input[i]
            s = self.epsilonClosure(self.transition(s, c))
            if s == -1:
                print("\nExecution cannot proceed:\n    Current symbol: {}".format(c))
                break
        
        print()

        to_print = "No"
        for state in s:
            if s in self.accepting_states:
                to_print = "Yes"

        print(to_print)

        # if str(s) in self.accepting_states:
        #     print("Yes")
        # else:
        #     print("No")

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
def generateNFA(filename):
    file = open(filename, 'r')

    lines = file.readlines()

    # get transition functions
    num_transitions = int(lines[5])
    transitions = []
    for i in range(6, 6 + num_transitions):
        transitions.append(lines[i].replace("\n", ""))

    # get null transition functions
    num_null_transitions = int(lines[6 + num_transitions])
    null_transitions = []
    for i in range(7 + num_transitions, 7 + num_transitions + num_null_transitions):
        null_transitions.append(lines[i].replace("\n", ""))

    nfa = NFA(
        int(lines[0].rstrip()), # number of states
        int(lines[1].rstrip()), # number of accepting states
        lines[2].rstrip(),      # list of accepting states
        int(lines[3].rstrip()), # number of chars in alphabet
        lines[4].replace("\n", ""), # chars in alphabet
        int(num_transitions),       # number of transitions
        transitions,                # transition functions
        int(num_null_transitions),  # number of null transitions
        null_transitions,           # null transition functions
        lines[6 + num_transitions].rstrip() # dfa input
    )

    return nfa

if __name__ == "__main__":
    nfa = generateNFA(sys.argv[1])
    nfa.simulateNFA()
