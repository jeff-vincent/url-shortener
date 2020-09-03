import string
import random
from flask import Flask
from flask import request
from flask import redirect
from peewee import *
from index import index_view
from index import index_view_w_response

app = Flask('__main__')
db = SqliteDatabase('urls.db')

class URLMapping(Model):
    url_hash = CharField()
    url = CharField()

    class Meta:
        database = db

HASH_LENGTH = 8

def initialize_db():
    db.connect()
    db.create_tables([URLMapping], safe = True)
    db.close()

@app.route('/', methods=['GET'])
def index():
	return index_view

@app.route('/i<url_hash>', methods=['GET'])
def forward_request(url_hash):
	url = get_url_by_hash(url_hash)
	full_url = 'https://{}'.format(url)
	return redirect(full_url)

@app.route('/shorten-url', methods=['POST'])
def shorten_url():
	url_to_shorten = request.form.get(
		'url_to_shorten').replace(
		'http://', '').replace('https://', '')

	exists = check_for_existing_match(url_to_shorten)

	if exists == 0:
		url_hash = get_random_string(HASH_LENGTH)
		write_url_to_db(url_hash, url_to_shorten)

	elif exists == 1:
		url_hash = get_hash_by_url(url_to_shorten)
		print(url_hash)

	host_url = request.host_url
	url = host_url+'i{}'.format(url_hash)
	return index_view_w_response.format(url, url)

def check_for_existing_match(url_to_shorten):
	try:
		mapping = URLMapping.get(
			URLMapping.url == url_to_shorten)
		return 1
	except:
		return 0

def write_url_to_db(url_hash, url):
	new_entry = URLMapping(
		url_hash=url_hash,
		url=url)
	new_entry.save()

def get_hash_by_url(url_to_shorten):
	mapping = URLMapping.get(
		URLMapping.url == url_to_shorten)
	url_hash = mapping.url_hash
	return url_hash

def get_url_by_hash(url_hash):
	mapping = URLMapping.get(
		URLMapping.url_hash == url_hash)
	url = mapping.url
	return url

def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(
    	random.choice(
    	letters) for i in range(length))
    return result_str


if __name__ == '__main__':
	initialize_db()
	app.run(debug=True)
