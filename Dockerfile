FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt \
&& rm -rf /tmp
COPY uwsgi.ini /app
COPY ./url_shortener /app/url_shortener

