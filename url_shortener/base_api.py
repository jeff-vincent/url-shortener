import string
import random
import requests
from db import URLMapping


class BaseAPI:

	def __init__(self):
		pass

	def check_for_existing_match(self, url_to_shorten):
		try:
			mapping = URLMapping.get(
				URLMapping.url == url_to_shorten)
			return 1
		except:
			return 0

	def write_url_to_db(self, url_hash, url):
		new_entry = URLMapping(
			url_hash=url_hash,
			url=url)
		new_entry.save()

	def get_hash_by_url(self, url_to_shorten):
		mapping = URLMapping.get(
			URLMapping.url == url_to_shorten)
		url_hash = mapping.url_hash
		return url_hash

	def get_url_by_hash(self, url_hash):
		mapping = URLMapping.get(
			URLMapping.url_hash == url_hash)
		url = mapping.url
		return url

	def get_random_string(self, length):
	    pool = string.ascii_letters + string.digits
	    result_str = ''.join(
	    	random.choice(pool) for i in range(length))
	    return result_str

	def chop_url(self, url):
		chopped_url = url.replace(
			'https://', '').replace(
			'http://', '')
		return chopped_url

	def check_connectivity(self, url):
		clean_url = self.chop_url(url)
		url_prefix = 'https://{}'
		full_url = url_prefix.format(clean_url)
		try:
			r = requests.get(full_url)
			response_code_list = r.status_code.split()
			if str(response_code_list[0]) != '4' \
			and str(response_code_list[0] != '5'):
				return 1
		except:
			return 0
