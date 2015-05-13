# -*- coding: utf-8 -*-
from endomondo import Endomondo

endomondo = Endomondo("dominik.jaguszewski@gmail.com", "")

try:
	endomondo.authenticate()
except ValueError:
	print "Authentication failed"
	quit()
except:
	print "Unknown error"
	quit()

print endomondo.authToken
print endomondo.secureToken
