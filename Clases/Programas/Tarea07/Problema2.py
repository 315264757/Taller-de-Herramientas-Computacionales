# !/usr/bin/python
# -*- coding: utf-8 -*-

rat = [1,2,3]
cat = [4,5,6]
bat = [7,8,9]

M = [[tar,tac,tab] for tar,tac,tab in zip(rat,cat,bat)]
    
c1 = sum(M[0])
c2 = sum(M[1])
c3 = sum(M[2])
f1 = sum(rat)
f2 = sum(cat)
f3 = sum(bat)

print '%1d %1d %1d' % (c1,c2,c3)
print '%1d %1d %1d' % (f1,f2,f3)
