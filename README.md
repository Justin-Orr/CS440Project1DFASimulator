# CS440 DFA Simulator
The goal is to write an OCaml or python program that reads a description of a DFA and an input string and runs the DFA to see whether or not it accepts the string. At each DFA step, you print out the state you're in and the terminal symbol you saw. At the end you print out the final state and whether or not it accepted.
## DFA Description Format
* One line with the number of states N in the DFA (the states will be 0 through N-1).
* One line with the number of accepting states in the DFA
* One line (for each accepting state) with the state number
* One line with the number of symbols M in the alphabet
* One line with the alphabet (M characters)
* One line with the number of transition cases
  * One line for each transition case: old-state comma symbol comma new-state.
* One line with the input to the DFA.
### Example of DFA Input
The DFA below has states 0 and 1 with 1 as the only accepting state, alphabet a, b, c, and space,
and seven transition function entries.<br /><br />
2          — Two states, 0, 1<br />
1          — One accepting state<br />
1          — 1 is an accepting state<br />
4          — 4 characters in the alphabet<br />
abc          — the characters are a, b, c, and space (hard to see, but it's the 4th character)<br />
7          — Number of transition function entries<br />
1,b,1          — In state 1, on b, go to state 1 [note the entries don't have to be sorted]<br />
1, a , 1          — In state 1, on a, go to state 1 [notice there exists whitespace]<br />
0, b, 0<br />
0,a, 1<br />
1, c,0<br />
0,,0          — In state 0, on space, go to state 0 [two commas imply space as input symbol]<br />
1 , , 1          — In state 1, on space, go to state 1 [two commas imply space as input symbol]<br />
bba aca          — The input to the DFA<br /><br />
The alphabet should include only individual characters (no escape sequences like \t). If a space
appears within the M characters of the alphabet, then a space is one of the M symbols. Similarly, if
a space appears in the DFA input, treat it as a symbol.<br /><br />
Print out a trace of information about the DFA as you read it. If you notice an error, you're allowed
to print an error message/raise an exception and halt. You're also allowed to wait until execution
of the DFA to realize there are errors in the transition function (bad state number, bad symbol,
multiple entries for the same state/symbol pair).<br /><br />
When you execute the DFA on the input, print a trace of the state, symbol, state, symbol, ...., state it
encounters. At the end, say whether or not the input is accepted. If you're in a state and the next
symbol has no transition function result defined, then stop execution and say what the input
symbol is and that you're stuck [execution cannot proceed]. Since not all the input has been
processed, it's automatically rejected.<br /><br />
[Hint: If you cause a runtime error or raise an exception, you might want to flush the output buffer
so that you don't lose part of the output.]<br /><br />
A sample trace for the DFA and input in the example above could be something like:<br /><br />
0 b 0 b 0 a 1 1 a 1 c 0 a 1   — space as 4th character.<br />
0 b 0 b 0 a 1 ' '1 a 1 c 0 a 1   — space as 4th character.<br /><br />
Your program should be organized so that at the top level of the read-eval-print loop, you can enter:<br /><br />
   simulate dfa "name of text file" or simulate dfa("name of text file")<br /><br />
as appropriate for OCaml or python.