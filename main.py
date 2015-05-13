# -*- coding: utf-8 -*-
from endomondo import Endomondo

endomondo = Endomondo("email", "pass")

test = endomondo.authenticate()
print test
print endomondo.authToken
print endomondo.secureToken
