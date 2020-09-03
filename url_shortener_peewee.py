import string
import random
from flask import Flask
from flask import request
from flask import redirect
from peewee import *

app = Flask('__main__')
db = SqliteDatabase('urls.db')

class URLMapping(Model):
    url_hash = CharField()
    url = CharField()

    class Meta:
        database = db

HASH_LENGTH = 8

@app.route('/i<url_hash>', methods=['GET'])
def forward_request(url_hash):
	url = get_url_from_db(url_hash)
	full_url = 'https://{}'.format(url)
	return redirect(full_url)


@app.route('/shorten-url', methods=['POST'])
def shorten_url():
	url_to_shorten = request.form.get(
				'url_to_shorten').replace(
				'http://', '').replace('https://', '')
	url_hash = get_random_string(HASH_LENGTH)
	host_url = request.host_url
	url = host_url+'i{}'.format(url_hash)
	write_url_to_db(url_hash, url_to_shorten)
	return url


def write_url_to_db(url_hash, url):
	new_entry = URLMapping(
			url_hash=url_hash,
			url=url)
	new_entry.save()


def get_url_from_db(url_hash):
	mapping = URLMapping.get(URLMapping.url_hash == url_hash)
	url = mapping.url
	return url

def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def initialize_db():
    db.connect()
    db.create_tables([URLMapping], safe = True)
    db.close()

if __name__ == '__main__':
	initialize_db()
	app.run(debug=True)

