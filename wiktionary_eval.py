from __future__ import division
import sys
import numpy as np
sys.path.append('hyperwords')
from representations.embedding import Embedding


Es = Embedding(sys.argv[1], True)
Et = Embedding(sys.argv[2], True)

BX = [(l.split("|||")[-1].strip(), l.split("|||")[0].strip()) for l in open(sys.argv[3]).readlines()]
if sys.argv[-1] == 'R':
   BX = [(t, s) for s, t in BX]
   Es, Et = Et, Es

BD=[]
for s,t in BX:
    if s in Es.wi and t in Et.wi:
        BD.append((s,t))

p1, tot = 0, 0
for s, t in BD:
    vs = Es.represent(s)
    scores = vs.dot(Et.m.T)
    cand = Et.iw[np.nanargmax(scores)]
    if t==cand:
        p1+=1
    tot+=1

print '{0:.4f}'.format(p1/tot)
