import nfa

nfa = nfa.generateNFA("input2.txt")
print(nfa.epsilonClosure(str(0)))