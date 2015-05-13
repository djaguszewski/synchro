# -*- coding: utf-8 -*-
from endomondo import Endomondo
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

endomondo = Endomondo("e@mail.com", "pass")

try:
	endomondo.authenticate()
except ValueError:
	print "Authentication failed"
	quit()
except:
	print "Unknown error"
	quit()

#print endomondo.authToken
#print endomondo.secureToken
