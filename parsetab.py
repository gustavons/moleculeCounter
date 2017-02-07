
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'ECABC82B260232D73F4710138374599C'
    
_lr_action_items = {'SIMBOLOS':([1,3,4,6,9,10,11,12,13,14,],[4,-8,-6,-2,4,-9,-11,4,4,4,]),'NUMBER':([1,3,4,6,9,10,11,12,13,14,],[6,-8,-6,-2,6,-9,-11,6,6,6,]),'IGUAL':([1,3,4,6,9,10,11,12,13,14,],[7,-8,-6,-2,7,-9,-11,7,7,7,]),'CEELE':([2,3,],[8,-5,]),'HASHTAG':([1,3,4,6,9,10,11,12,13,14,],[5,-8,-6,-2,5,-9,-11,5,5,5,]),'ELEMENTO':([0,4,5,6,7,8,],[3,3,11,3,3,3,]),'$end':([1,3,4,6,9,10,11,12,13,14,],[0,-8,-6,-2,-7,-9,-11,-3,-1,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,4,6,7,8,],[1,9,12,13,14,]),'ce':([0,4,6,7,8,],[2,2,2,2,2,]),'factor':([5,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> term","S'",1,None,None,None),
  ('term -> term IGUAL term','term',3,'p_expression_igual','mainContagem.py',17),
  ('term -> term NUMBER','term',2,'p_expression_number','mainContagem.py',41),
  ('term -> term NUMBER term','term',3,'p_expression_number_junto','mainContagem.py',43),
  ('term -> ce CEELE term','term',3,'p_expression_ceele','mainContagem.py',46),
  ('ce -> ELEMENTO','ce',1,'p_expression_ce','mainContagem.py',66),
  ('term -> term SIMBOLOS','term',2,'p_expression_simbolos','mainContagem.py',68),
  ('term -> term SIMBOLOS term','term',3,'p_expression_simbolos_junto','mainContagem.py',71),
  ('term -> ELEMENTO','term',1,'p_expression_nada','mainContagem.py',78),
  ('term -> term HASHTAG factor','term',3,'p_term_hashtag','mainContagem.py',114),
  ('expression -> term SIFRAO factor','expression',3,'p_term_sifrao','mainContagem.py',120),
  ('factor -> ELEMENTO','factor',1,'p_factor_num','mainContagem.py',130),
]
