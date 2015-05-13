# -*- coding: utf-8 -*-
#Methods for connecting to Endomondo

import requests

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
		splitted_response = response.text.split("\n")

		if splitted_response[0] != "OK":
			self.authToken = -1
			self.secureToken = -1
			return -1
		else:
			for line in splitted_response:
				if "authToken" in line:
					key,value = line.split("=")
					self.authToken = value
				if "secureToken" in line:
					key,value = line.split("=")
					self.secureToken = value
			return 0
