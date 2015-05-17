# -*- coding: utf-8 -*-
from endomondo import Endomondo
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

endomondo = Endomondo("user", "pass")

try:
	endomondo.authenticate()
except ValueError:
	print "Authentication failed"
	quit()
except:
	print "Unknown error"
	quit()

endomondo.get_user_data()
