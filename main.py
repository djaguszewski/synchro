# -*- coding: utf-8 -*-
from endomondo import Endomondo

endomondo = Endomondo("em@ai.l", "pass")

test = endomondo.authenticate()
print test['auth']
print test['sec']
