# url-shortener

A simple URL shortener written in Flask. 

## Run it locally
### 1. Update file `/url_shortener/db.py` as follows:

`db = PostgresqlDatabase('url_shortener', user='postgres', password='password',
                           host='db', port=5432)`
##### Needs to be changed to:

`db = PostgresqlDatabase('url_shortener', user='postgres', password='password',
                           host='0.0.0.0', port=5432)`

### 2. Start Postgres

```
docker run \
-e POSTGRES_USER=postgres \
-e POSTGRES_DB=url_shortener \
-e POSTGRES_PASSWORD=password \
-p 5432:5432 \
--name postgres-db \
postgres
```

### 3. Start app
`python url_shortener.py`

## Deploy in Docker
`docker-compose -f url_shortener.yml up`
