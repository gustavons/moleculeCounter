from nltk import Nonterminal, nonterminals, Production, CFG
nt1 = Nonterminal('NP')
nt2 = Nonterminal('VP')
S, NP, VP, PP = nonterminals('S, NP, VP, PP')
N, V, P, DT = nonterminals('N, V, P, DT')
prod1 = Production(S, [NP, VP])
prod2 = Production(NP, [DT, NP])

grammar = CFG.fromstring("""
    S -> 'C'S | 'O'S | 'N'S | 'S'S | 'F'S | 'H'S | 'B'S | '1'S | '2'S | '+'S
    S -> '3'S | '='S | '('S | ')'S | '['S | ']'S | '@'S | '/'S | '\\'S
    S -> 'C' | 'O' | 'N' | 'S' | 'F' | 'H' | 'B' | '1' | '2' | '+'
    S -> '3' | '=' | '(' | ')' | '[' | ']' | '@' | '/' | '\\'
    """)


from nltk.parse import RecursiveDescentParser
rd = RecursiveDescentParser(grammar)
from nltk.parse import RecursiveDescentParser
rd = RecursiveDescentParser(grammar)
# sentence1 = 'the cat chased the dog'.split()
# sentence2 = 'the cat chased the dog on the rug'.split()
sente1 = 'CC\C=C/C\C=C/C\C=C/CCCCCCCC(O)=O'
sentence1 = []
for carac in sente1:
    sentence1.append(carac)

for t in rd.parse(sentence1):
    print(t)