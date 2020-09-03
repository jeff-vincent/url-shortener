import string
import random
from flask import Flask
from flask import request
from flask import redirect

app = Flask('__main__')

HASH_LENGTH = 8

@app.route('/i<_hash>', methods=['GET'])
def forward_request(_hash):
	url = get_url_from_db(_hash)
	full_url = 'https://{}'.format(url)
	return redirect(full_url)


@app.route('/shorten-url', methods=['POST'])
def shorten_url():
	url_to_shorten = request.form.get(
					'url_to_shorten').replace(
					'http://', '').replace('https://', '')
	_hash = get_random_string(HASH_LENGTH)
	host_url = request.host_url
	url = host_url+'i{}'.format(_hash)
	write_url_to_db(_hash, url_to_shorten)
	return url


def write_url_to_db(_hash, url):
	with open('db.txt', 'a') as db:
		db.write('{}|{}\n'.format(_hash, url))


def get_url_from_db(_hash):
	with open('db.txt', 'r') as db:
		for line in db:
			if _hash in line:
				line_list = line.split('|')
				url = line_list[1].replace('\n', '')
				return url


def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

if __name__ == '__main__':
	app.run(debug=True)