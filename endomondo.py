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
	__authentication_url = "https://api.mobile.endomondo.com/mobile/auth"
	#User profile
	__user_profile_url = "https://api.mobile.endomondo.com/mobile/api/profile/account/get"
		
	__authToken = None;
	__secureToken = None;

	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.request = requests.session()
		
	def authenticate(self):
		'''
		authenticate
		It gets username (email) and password and returns two tokens

		If authentication is successfull it returns 0

		If authentication fails it returns -1
		'''

		request_url = self.__authentication_url
		request_params = {
			'deviceId' : 'test', 
			'email' : self.username, 
			'password' : self.password, 
			'country' : 'UK', 
			'action' : 'pair'}

		response = self.request.get(request_url,params=request_params)
		logging.debug("Request params: " + str(request_params))
		splitted_response = response.text.split("\n")

		if splitted_response[0] != "OK":
			self.__authToken = -1
			self.__secureToken = -1
			logging.critical("Authentication failed. Server response: %s" %response.text)
			raise AuthenticationError("Authentication problem: %s" % splitted_response[0])
		else:
			for line in splitted_response:
				if "authToken" in line:
					try:
						key,value = line.split("=")
					except:
						logging.critical("Error while parsing athentication token " + line)
						return
					self.__authToken = value
				if "secureToken" in line:
					try:
						key,value = line.split("=")
					except:
						logging.critical("Error while parsing authentication token " + line)
						return
					self.__secureToken = value

	def get_authentication_token(self):
		return self.__authToken
		
	def get_secure_token(self):
		return self.__secureToken
			
	def get_user_data(self):
		authToken = self.get_authentication_token();
		#TODO: build and send request, parse user data and create variables in class
		print authToken
