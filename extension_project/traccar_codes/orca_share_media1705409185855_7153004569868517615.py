"""
BASED ON TRACCAR API - with modification
	https://github.com/Silverdoses/pytraccar/tree/master/pytraccar

"""
import websocket
import requests
import json
from threading import Thread
import urllib
import rel

# pip install rel
class API_Traccar:
	def __init__(self, host):
		self.__urls ={
			'session': "http://" + host + '/api/session',
			'devices': "http://" + host + '/api/devices',
			'positions': "http://" + host + '/api/position',
			'notifications': "http://" + host + '/api/notifications',
			'events': "http://" + host + '/api/events', # /events/{id} where id is required
			'geofences': "http://" + host + '/api/geofences'
		}
		self.__token = ''
		self.__sess = requests.Session()


	def show_token(self):
		return self.__token


	def token_auth(self, token):
		url = self.__urls['session']
		params = {'token': token}
		response = self.__sess.post(url=url, data=params)

		if response.status_code == 200:  # OK
			self.__token = token
			return response.json()
		elif response.status_code == 404:  # Invalid token
			# raise invalid token exception here
			pass
		else:
			# raise API exeption
			pass


	def credential_auth(self, email, password):
		url = self.__urls['session']
		credentials = {'email':email, 'password':password}
		response = self.__sess.post(url=url, data=credentials)

		if response.status_code == 200:  # OK
			return response.json()
		elif response.status_code == 401:  # Invalid credentials
			# raise invalid credentials exception here
			pass
		else:
			# raise API exeption
			pass


	def get_all_devs(self):
		url = self.__urls['devices']
		query_params = {'all': True}
		response = self.__sess.get(url=url, params=query_params)

		if response.status_code == 200:  # OK
			return response.json()
		elif response.status_code == 401:  # Invalid credentials
			# raise invalid credentials exception here
			pass
		else:
			# raise API exeption
			pass

	def get_spec_devs(self, query=None, params=None):
		url = self.__urls['devices']

		if not query:
			response = self.__sess.get(url=url)
		else:
			data_params = {query: params}  # {id: 0}
			response = self.__sess.get(url=url, params=data_params)
		
		if response.status_code == 200:  # OK
			return response.json()
		elif response.status_code == 400:  # not found
			# raise no object found exception here
			pass
		else:
			# raise API exeption
			pass

	def get_pos(self):  # get positions, but traccar recommends using the websocket API for real time positions
		pass


	def get_all_notifs(self):
		url = self.__urls['notifications']
		query_params = {'all': True}
		response = self.__sess.get(url=url, params=query_params)

		if response.status_code == 200:  # OK
			return response.json()
		elif response.status_code == 401:  # Invalid credentials
			# raise invalid credentials exception here
			pass
		else:
			# raise API exeption
			pass


	def get_dev_notif(self, query=None, params=None):  # not need for now
		url = self.__urls['notifications']

		if not query:
			response = self.__sess.get(url=url)
		else:
			data_params = {query: params}  # {id: 0}
			response = self.__sess.get(url=url, params=data_params)

		if response.status_code == 200:  # OK
			return response.json()
		elif response.status_code == 400:  # not found
			# raise no object found exception here
			pass
		else:
			# raise API exeption
			pass


	def get_events(self, id):
		url = self.__urls['events'] + "/" + str(id)
		response = self.__sess.get(url=url)

		if response.status_code == 200:
			return response.json()
		elif response.status_code == 400:  # not found
			# raise no object found exception here
			pass
		else:
			# raise API exeption
			pass


	def get_dev_id(self, data):  # return a dictionary of all devices with corresponding...
								 # ...name and id as key-value pairs
		dev_id = {}
		for dev in data:
			dev_id[dev['id']] = dev['name']
		
		return dev_id


	def get_all_geof(self):
		url = self.__urls['geofences']
		query_params = {'all': True}
		response = self.__sess.get(url=url, params=query_params)

		if response.status_code == 200:  # OK
			return response.json()
		elif response.status_code == 401:  # Invalid credentials
			# raise invalid credentials exception here
			pass
		else:
			# raise API exeption
			pass	


	def get_geof_id(self, data):
		geof_id = {}
		for geof in data:
			geof_id[geof['id']] = geof['name']

		return geof_id





		
