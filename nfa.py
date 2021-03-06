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


    def epsilonClosure(self, S, paths):
        # print(S)
        for i in range(0, len(S)):
            for null_transition in self.null_transitions:
                if null_transition[0] == str(S[i]):
                    if int(null_transition[-1]) not in S: # ensuring no duplicates are added to the set of reachable states
                        S.append(int(null_transition[-1]))
                        if int(null_transition[-1]) not in paths.keys():
                            paths[int(null_transition[-1])] = ['ε']
                        else:
                            if 'ε' not in paths[int(null_transition[-1])]:
                                paths[int(null_transition[-1])].append('ε')
        return S


    def simulateNFA(self):

        print("\nNOTICE: A state value of -1 specifies a dead state. Dead states are handled with an error message and the program continues to execute.\n")

        # determining epsilonClosure for the initial state
        paths = {}
        S = self.epsilonClosure([0], paths)

        for i in range(0, len(self.nfa_input)):
            c = self.nfa_input[i]
            print('Current char: {}\nPossible current states prior to transition: {}'.format(c, S))
            S = self.epsilonClosure(self.transition(S, c, paths), paths)
            c_states = []
            e_states = []
            for s in S:
                for k, v in paths.items():
                    if k == s:
                        for t in self.transitions:
                            new_t = t.replace(' ', '').split(',')
                            if c in new_t:
                                if s == int(new_t[0]):
                                    if c in v:
                                        c_states.append(k)
                        for n in self.null_transitions:
                            if s == int(n[0]):
                                e_states.append(int(n[-1]))
                        

            print('Possible states after transition: {}'.format(S))

            for state in S:
                if state == -1:
                    print("   Error: Dead state was found. Removing from list of current possible states and continuing.")
                    S.remove(-1)

            print('Reachable states using {}: {}\nReachable states using ε: {}\n'.format(c, c_states, e_states))

        print()

        to_print = "No"
        for state in S:
            if state in self.accepting_states:
                to_print = "Yes"

        print(to_print)

    # c being equal to a space character is the same as an empty string in our transition table
    # based on the project description. Therefore in order to handle c for this case, we must 
    # compare to see if it is equal to a space character and simultaneously see if the character 
    # in the transition function is equal to empty string
    def transition(self, S, c, paths):
        # iterate over every state within S
        for i in range(0, len(S)):
            found_match = False
            # Check if c is an empty string, if so then check null-transition functions
            if c == '':
                for t in self.null_transitions: 
                    new_t = t.replace(' ', '').split(',') # take transition string and break up into a list of tokens
                    if int(new_t[0]) == S[i]:
                        found_match = True
                        if int(new_t[1]) not in S:
                            print(new_t[0], S[i], new_t[1])
                            S[i] = int(new_t[1])

            temp = {} # stores values that need to be updated after transition

            # Check state using base transition functions
            for t in self.transitions:                 
                new_t = t.replace(' ', '').split(',') # take transition string and break up into a list of tokens
                if int(new_t[0]) == S[i]:
                    if new_t[1] == c:
                        temp[i] = int(new_t[2])
                        found_match = True
                        
                        # updating what state c leads to
                        if (int(new_t[2]) not in paths.keys()):
                            paths[int(new_t[2])] = [c]
                        else:
                            if c not in paths[int(new_t[2])]:
                                paths[int(new_t[2])].append(c)
                        
                    elif c == ' ' and new_t[1] == '':
                        found_match = True
                        if int(new_t[2]) not in S:
                            S[i] = int(new_t[2])

            for k, v in temp.items():
                S[k] = v
                
            if not found_match:
                S[i] = -1

        return S

# generates a DFA object from an input file
def generateNFA(filename):
    file = open(filename, 'r')

    lines = file.readlines()
    line_index = 0

    num_of_states = int(lines[line_index].rstrip())
    line_index = line_index + 1
    #print("value: " + str(num_of_states) + " new line index: " + str(line_index))

    # get all acceptance states
    num_of_acceptance_states = int(lines[line_index])
    acc_states = []
    for i in range(line_index + 1, line_index + num_of_acceptance_states + 1):
        acc_states.append(int(lines[i].replace("\n", "")))
    line_index = line_index + num_of_acceptance_states + 1
    #print("num_of_acceptance_states: " + str(num_of_acceptance_states) + " states: " + str(acc_states) + " new line index: " + str(line_index))

    # grab characters in alphabet
    num_of_symbols = int(lines[line_index].rstrip())
    line_index = line_index + 1
    char_in_alph = lines[line_index].replace("\n", "")
    line_index = line_index + 1
    #print("num_of_symbols: " + str(num_of_symbols) + " char_in_alph: " + str(char_in_alph) + " new line index: " + str(line_index))

    # get transition functions
    num_of_transitions = int(lines[line_index].rstrip())
    transitions = []
    for i in range(line_index + 1, line_index + num_of_transitions + 1):
        transitions.append(lines[i].replace("\n", ""))
    line_index = line_index + num_of_transitions + 1
    #print("num_of_transitions: " + str(num_of_transitions) + " transitions: " + str(transitions) + " new line index: " + str(line_index))

    # get null transition functions
    num_of_null_trans = int(lines[line_index])
    null_transitions = []
    for i in range(line_index + 1, line_index + num_of_null_trans + 1):
        null_transitions.append(lines[i].replace("\n", ""))
    line_index = line_index + num_of_null_trans + 1
    #print("num_of_null_trans: " + str(num_of_null_trans) + " null_transitions: " + str(null_transitions) + " new line index: " + str(line_index))

    # grab starting index for input
    input_string = lines[line_index].rstrip()
    #print("input string: " + input_string)

    nfa = NFA(
        num_of_states, # number of states
        num_of_acceptance_states, # number of accepting states
        acc_states,      # list of accepting states
        num_of_symbols, # number of chars in alphabet
        char_in_alph, # chars in alphabet
        num_of_transitions,       # number of transitions
        transitions,                # transition functions
        num_of_null_trans,  # number of null transitions
        null_transitions,           # null transition functions
        input_string # dfa input
    )

    return nfa

if __name__ == "__main__":
    nfa = generateNFA(sys.argv[1])
    nfa.simulateNFA()
