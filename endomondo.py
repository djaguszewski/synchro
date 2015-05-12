# -*- coding: utf-8 -*-
#Methods for connecting to Endomondo

import requests

class Endomondo:
	#URL's used in connectivity with Endomondo
	#Authentication:
	authentication_url = "https://api.mobile.endomondo.com/mobile/auth"	

	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.request = requests.session()
	
	'''
	authenticate
	It gets username (email) and password and returns two tokens

	If authentication is successfull it returns:
	[{authenticationToken},{secureToken}]

	If authentication fails it returns:
	[-1,-1]
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
		'''
			OK
			action=PAIRED
			authToken=ica0eL1oQJKp57bmbxK8Wg
			measure=METRIC
			displayName=Dominik Jaguszewski
			userId=12112903
			facebookConnected=true
			secureToken=8DdL3EE-Qn2AUSSeEQ_L5g
		'''
		exit_values = {'auth' : 0, 'sec': 0}
		if splitted_response[0] != "OK":
			exit_values = {'auth' : -1, 'sec': -1}
		else:
			splitted_response.pop(0)
			for line in splitted_response:
				key,value = line.split("=")
				if key=="authToken":
					exit_values['auth']=value
				if key=="secureToken":
					exit_values['sec']=value
					break
		return exit_values
