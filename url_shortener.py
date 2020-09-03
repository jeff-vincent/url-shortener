import configparser
from flask import Flask
from flask import request
from flask import redirect
from base_api import BaseAPI
from index import index_view
from index import index_view_w_response

app = Flask('__main__')
base = BaseAPI()
config = configparser.ConfigParser()
config.read('url_shortener.cfg')

@app.route('/', methods=['GET'])
def index():

	return index_view


@app.route('/i<url_hash>', methods=['GET'])
def forward_request(url_hash):
	url = base.get_url_by_hash(url_hash)
	full_url = 'https://{}'.format(url)

	return redirect(full_url)


@app.route('/shorten-url', methods=['POST'])
def shorten_url():
	raw_url = request.form.get('url_to_shorten')
	url_to_shorten = base.chop_url(raw_url)

	exists = base.check_for_existing_match(url_to_shorten)

	if exists:
		url_hash = base.get_hash_by_url(url_to_shorten)

	else:
		url_hash = base.get_random_string(
			int(config['setup']['hash_length']))
		print(url_hash)
		base.write_url_to_db(url_hash, url_to_shorten)

	host_url = request.host_url
	url = host_url+'i{}'.format(url_hash)
	display_url = base.chop_url(url)

	return index_view_w_response.format(url,display_url)


if __name__ == '__main__':
	app.run(debug=True)
