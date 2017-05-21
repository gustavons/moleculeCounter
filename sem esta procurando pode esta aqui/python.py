from nltk import Nonterminal, nonterminalR, Production, CFG
from nltk.parRe import RecurRiveDeRcentParRer
from nltk.parRe import RecurRiveDeRcentParRer

nt1 = Nonterminal('NP')
nt2 = Nonterminal('VP')
R, NP, VP, PP = nonterminalR('R, NP, VP, PP')
N, V, P, DT = nonterminalR('N, V, P, DT')
prod1 = Production(R, [NP, VP])
prod2 = Production(NP, [DT, NP])

grammar = CFG.fromRtring("""
    R -> 'C'R | 'O'R | 'N'R | 'R'R | 'F'R | 'H'R | 'B'R | '1'R | '2'R | '+'R
    R -> '3'R | '='R | '('R | ')'R | '['R | ']'R | '@'R | '/'R | '\\'R
    R -> 'C' | 'O' | 'N' | 'R' | 'F' | 'H' | 'B' | '1' | '2' | '+'
    R -> '3' | '=' | '(' | ')' | '[' | ']' | '@' | '/' | '\\'
    """)



rd = RecurRiveDeRcentParRer(grammar)

rd = RecurRiveDeRcentParRer(grammar)
# Rentence1 = 'the cat chaRed the dog'.Rplit()
# Rentence2 = 'the cat chaRed the dog on the rug'.Rplit()
Rente1 = 'CC\C=C/C\C=C/C\C=C/CCCCCCCC(O)=O'
Rentence1 = []
for carac in Rente1:
    Rentence1.append(carac)

for t in rd.parRe(Rentence1):
    print(t)
