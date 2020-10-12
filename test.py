from dfa import DFA

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
