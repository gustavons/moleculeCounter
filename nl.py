from nltk import Nonterminal, nonterminals, Production, CFG
S = Nonterminal('S')
prod1 = Production(S, [])

grammar = CFG.fromstring("""
    S -> 'C'S | 'O'S | 'N'S | 'S'S | 'F'S | 'H'S | 'B'S | '1'S | '2'S | '+'S | '%'S
    S -> '3'S | '4'S | '='S | '('S | ')'S | '['S | ']'S | '@'S | '/'S | '\\'S | 'CL'S
    S -> 'C' | 'O' | 'N' | 'S' | 'F' | 'H' | 'B' | '1' | '2' | '+' | 'CL'
    S -> '3' | '%' | '4' | '=' | '(' | ')' | '[' | ']' | '@' | '/' | '\\'
    """)

from nltk.parse import RecursiveDescentParser
rd = RecursiveDescentParser(grammar)
sente1 = 'NC1=NC(=O)C2=C(NCC(CNC3=CC=C(C=C3)C(=O)N[C@@H](CCC(O)=O)C(O)=O)N2)N1'
sentence1 = []
for carac in sente1:
    sentence1.append(carac)

for t in rd.parse(sentence1):
    print(t)