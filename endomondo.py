# -*- coding: utf-8 -*-
#Methods for connecting to Endomondo

import requests, logging

class AuthenticationError(ValueError):
	'''
	Authentication unsuccessfull
	'''

class UserDataError(ValueError):
	'''
	User data cannot be received
	'''

class Endomondo:
	#URL's used in connectivity with Endomondo
	#Authentication:
	__authentication_url = "https://api.mobile.endomondo.com/mobile/auth"
	#User profile
	__user_profile_url = "https://api.mobile.endomondo.com/mobile/api/profile/account/get"
	
	#Tokens	
	__authToken = None;
	__secureToken = None;
	
	#User profile
	__user_data = {
		'id': None,
		'first_name': None,
		'last_name': None,
		'email': None,
		'phone_number' : None,
		'date_of_birth': None,
		'account_created' : None,
		'sex': None,
		'country' : None,
		'time_zone' : None,
		'last_sync' : None,
		'units' : None,
		'height_cm' :None,
		'weight_kg': None,
		'weight_time': None,
		'hr_zones': {
			'hr0': None,
			'hr1': None,
			'hr2': None,
			'hr3': None,
			'hr4': None,
			'hr5': None,
			'hrm': None
			}
		}

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
	
	def __send_get_request(self, request_url, params):
		params = {
			'authToken' : self.get_authentication_token(),
			'language' : 'en'}
						
		response = self.request.get(request_url, params=params)
		if response.status_code != requests.codes.ok:
			logging.CRITICAL("User data receiving problem. Request failed")
			raise UserDataError("User data receiving problem: %s" % response.text)
		return response
	
	def download_user_data(self):
		user_data = self.__send_get_request(self.__user_profile_url,{}).json()['data']
		self.__user_data['id'] = user_data['id']
		self.__user_data['first_name'] = user_data['first_name']
		self.__user_data['last_name'] = user_data['last_name']
		self.__user_data['email'] = user_data['email']
		self.__user_data['phone_number'] = user_data['phone']
		date_of_birth = user_data['date_of_birth'].split(" ")
		self.__user_data['date_of_birth'] = date_of_birth[0]
		self.__user_data['account_created'] = user_data['created_time']
		self.__user_data['sex'] = user_data['sex']
		self.__user_data['country'] = user_data['country']
		self.__user_data['time_zone'] = user_data['time_zone']
		self.__user_data['last_sync'] = user_data['sync_time']
		self.__user_data['units'] = user_data['units']
		self.__user_data['height_cm'] = user_data['height_cm']
		self.__user_data['weight_kg'] = user_data['weight_kg']
		self.__user_data['weight_time'] = user_data['weight_time']
		self.__user_data['hr_zones']['hr0'] = user_data['hr_zones']['rest']
		self.__user_data['hr_zones']['hr1'] = user_data['hr_zones']['z1']
		self.__user_data['hr_zones']['hr2'] = user_data['hr_zones']['z2']
		self.__user_data['hr_zones']['hr3'] = user_data['hr_zones']['z3']
		self.__user_data['hr_zones']['hr4'] = user_data['hr_zones']['z4']
		self.__user_data['hr_zones']['hr5'] = user_data['hr_zones']['z5']
		self.__user_data['hr_zones']['hrm'] = user_data['hr_zones']['max']
	
	def get_user_data(self):
		return self.__user_data;
