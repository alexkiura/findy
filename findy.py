from pprint import pprint
import json
import urllib.parse
import urllib.request
import sys

"""A  Python client calling Knowledge Graph Search API."""

def search_person(name):
	'''Searches for a person named name using the Google Knowledge Graph API 
		and returns the top most result '''

	api_key = 'AIzaSyDcDcyS-6YbYiv6ZBXjUnzsL43cpYzKXWA'
	query = name
	api_url = 'https://kgsearch.googleapis.com/v1/entities:search'
	params = {
	    'query': query,
	    'limit': 1,
	    'indent': True,
	    'key': api_key,
	    'prefix': True,
	    'types': 'Person'
	}

	url = api_url + '?' + urllib.parse.urlencode(params)
	str_response = urllib.request.urlopen(url).read().decode('utf-8')
	response = json.loads(str_response)

	default = 'Not available'

	def get_in_dict(dct, *keys):
		for key in keys:
			try:
				dct = dct[key]
			except KeyError:
				return 'Not Available'
		return dct


	for id, element in enumerate(response['itemListElement']):

	  print(get_in_dict(element['result'], 'name'), '\n')
	  try:
	  	print('Brief Summary:')
	  	pprint(get_in_dict(element['result']['detailedDescription'],'articleBody'))
	  	print('\nSource:', get_in_dict(element['result']['detailedDescription'],'url'))

	  except KeyError:
	  	print(default)

if len(sys.argv) <= 1:
	search_person('Linus Torvalds')
else:
	search_person(sys.argv[1])


