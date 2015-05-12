# -*- coding: utf-8 -*-
from endomondo import Endomondo

endomondo = Endomondo("dominik.jaguszewski@gmail.com", "domcio11")

test = endomondo.authenticate()
print test['auth']
print test['sec']
