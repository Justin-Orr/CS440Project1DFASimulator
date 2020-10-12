import test

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

    def printInfo(self):
        print('num_states: {}'.format(self.number_of_states))
        print('num_accepting_states: {}'.format(self.number_of_accepting_states))
        print('accepting_states: {}'.format(self.accepting_states))
        print('num_of_alphabet_chars: {}'.format(self.num_of_alphatbet_chars))
        print('alphabet_chars: {}'.format(self.alphabet_chars))
        print('num_transitions: {}'.format(self.num_of_transitions))
        print('transitions: {}'.format(self.transitions))
        print('dfa_input: {}'.format(self.dfa_input))

    def simulateDFA(self):
        s = 0
        c = self.dfa_input[0]
        
        for i in range(1, len(self.dfa_input)):
            s = self.transition(s, c)
            c = self.dfa_input[i]
        
        if s in self.accepting_states:
            return "Yes"
        else:
            return "No"

    def transition(self, s, c):

        return 0


    # DFA psuedocode
    '''
    s = starting state
    c = next char
    while(c != eof):
        s = move(s, c)
        c = nextChar()
    if s in accepting_states:
        return "Yes"
    else:
        return "No"
    '''

if __name__ == "__main__":
    dfa = test.generateDFA('input.txt')
    dfa.printInfo()
    print(len(dfa.alphabet_chars))


