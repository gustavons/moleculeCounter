
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER ELEMENTO IGUAL SIFRAO HASHTAG SIMBOLOS CEELEterm :  term IGUAL termterm : ce CEELE termterm : ce CEELEce : ELEMENTOterm :  term NUMBERterm :  term NUMBER termterm :  term SIMBOLOSterm :  term SIMBOLOS termterm : ELEMENTOterm : term HASHTAG termterm :  term SIFRAO termterm : SIMBOLOS termterm : SIMBOLOSterm : NUMBER term'
    
_lr_action_items = {'SIMBOLOS':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[2,6,2,2,-9,2,2,2,2,2,6,6,2,6,6,6,6,6,6,]),'NUMBER':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[3,7,3,3,-9,3,3,3,3,3,7,7,3,7,7,7,7,7,7,]),'IGUAL':([1,2,5,6,7,11,12,13,14,15,16,17,18,19,],[8,-13,-9,-7,-5,8,8,-3,8,8,8,8,8,8,]),'CEELE':([4,5,],[13,-4,]),'HASHTAG':([1,2,5,6,7,11,12,13,14,15,16,17,18,19,],[9,-13,-9,-7,-5,9,9,-3,9,9,9,9,9,9,]),'SIFRAO':([1,2,5,6,7,11,12,13,14,15,16,17,18,19,],[10,-13,-9,-7,-5,10,10,-3,10,10,10,10,10,10,]),'$end':([1,2,5,6,7,11,12,13,14,15,16,17,18,19,],[0,-13,-9,-7,-5,-12,-14,-3,-8,-6,-1,-10,-11,-2,]),'ELEMENTO':([0,2,3,6,7,8,9,10,13,],[5,5,5,5,5,5,5,5,5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,2,3,6,7,8,9,10,13,],[1,11,12,14,15,16,17,18,19,]),'ce':([0,2,3,6,7,8,9,10,13,],[4,4,4,4,4,4,4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> term","S'",1,None,None,None),
  ('term -> term IGUAL term','term',3,'p_expression_igual','mainContagemPronto.py',18),
  ('term -> ce CEELE term','term',3,'p_expression_ceele','mainContagemPronto.py',36),
  ('term -> ce CEELE','term',2,'p_so_ceele','mainContagemPronto.py',51),
  ('ce -> ELEMENTO','ce',1,'p_expression_ce','mainContagemPronto.py',66),
  ('term -> term NUMBER','term',2,'p_expression_number','mainContagemPronto.py',70),
  ('term -> term NUMBER term','term',3,'p_expression_number_junto','mainContagemPronto.py',73),
  ('term -> term SIMBOLOS','term',2,'p_expression_simbolos','mainContagemPronto.py',76),
  ('term -> term SIMBOLOS term','term',3,'p_expression_simbolos_junto','mainContagemPronto.py',79),
  ('term -> ELEMENTO','term',1,'p_expression_nada','mainContagemPronto.py',83),
  ('term -> term HASHTAG term','term',3,'p_term_hashtag','mainContagemPronto.py',114),
  ('term -> term SIFRAO term','term',3,'p_term_sifrao','mainContagemPronto.py',132),
  ('term -> SIMBOLOS term','term',2,'p_simbolos_juntos','mainContagemPronto.py',149),
  ('term -> SIMBOLOS','term',1,'p_simbol','mainContagemPronto.py',152),
  ('term -> NUMBER term','term',2,'p_simbolos','mainContagemPronto.py',155),
]
