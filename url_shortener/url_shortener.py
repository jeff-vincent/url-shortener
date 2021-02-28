from flask import Flask
from flask import request
from flask import redirect
from base_api import BaseAPI
from index import index_view
from index import index_view_w_response
from index import confirmation_view

app = Flask('__main__')
base = BaseAPI()

@app.route('/', methods=['GET'])
def index():

	return index_view


@app.route('/i<url_hash>', methods=['GET'])
def forward_request(url_hash):
	url = base.get_url_by_hash(url_hash)
	url_prefix = 'https://{}'
	full_url = url_prefix.format(url)

	return redirect(full_url)


@app.route('/shorten-url', methods=['POST'])
def shorten_url():
	raw_url = request.form.get('url_to_shorten')
	confirmed = request.form.get('confirmed')

	url_to_shorten = base.chop_url(raw_url)
	exists = base.check_for_existing_match(url_to_shorten)

	if exists:
		url_hash = base.get_hash_by_url(url_to_shorten)

	else:
		connects = base.check_connectivity(raw_url)

		if connects:
			url_hash = base.get_random_string(5)
			base.write_url_to_db(url_hash, url_to_shorten)

		elif not confirmed:
			return confirmation_view.format(raw_url)

		else:
			url_hash = base.get_random_string(5)
			base.write_url_to_db(url_hash, url_to_shorten)

	host_url = request.host_url
	url = host_url+'i{}'.format(url_hash)
	display_url = base.chop_url(url)

	return index_view_w_response.format(url,display_url)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8888)
