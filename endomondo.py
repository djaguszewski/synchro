# -*- coding: utf-8 -*-
#Methods for connecting to Endomondo

import requests, logging

class AuthenticationError(ValueError):
	'''
	Authentication unsuccessfull
	'''

class Endomondo:
	#URL's used in connectivity with Endomondo
	#Authentication:
	authentication_url = "https://api.mobile.endomondo.com/mobile/auth"	
	authToken = None;
	secureToken = None;

	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.request = requests.session()
	
	'''
	authenticate
	It gets username (email) and password and returns two tokens

	If authentication is successfull it returns 0

	If authentication fails it returns -1
	'''
	
	def authenticate(self):
		request_url = self.authentication_url
		request_params = {
			'deviceId' : 'test', 
			'email' : self.username, 
			'password' : self.password, 
			'country' : 'UK', 
			'action' : 'pair'}

		response = self.request.get(self.authentication_url,params=request_params)
		logging.debug("Request params: " + str(request_params))
		splitted_response = response.text.split("\n")

		if splitted_response[0] != "OK":
			self.authToken = -1
			self.secureToken = -1
			logging.critical("Authentication failed. Server response: %s" %response.text)
			raise AuthenticationError("Authentication problem: %s" % splitted_response[0])
		else:
			for line in splitted_response:
				if "authToken" in line:
					try:
						key,value = line.spllit("=")
					except:
						logging.critical("Error while parsing athentication token " + line)
						return
					self.authToken = value
				if "secureToken" in line:
					try:
						key,value = line.split("=")
					except:
						logging.critical("Error while parsing authentication token " + line)
						return
					self.secureToken = value
