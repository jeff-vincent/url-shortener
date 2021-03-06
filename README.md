# url-shortener

A simple URL shortener. 

## Run it locally

#### Requires 
- Python3.9

#### 1. Update file `/url_shortener/db.py` as follows:

`db = PostgresqlDatabase('url_shortener', user='postgres', password='password',
                           host='db', port=5432)`
##### Needs to be changed to:

`db = PostgresqlDatabase('url_shortener', user='postgres', password='password',
                           host='0.0.0.0', port=5432)`

#### 2. Start Postgres

```
docker run \
-e POSTGRES_USER=postgres \
-e POSTGRES_DB=url_shortener \
-e POSTGRES_PASSWORD=password \
-p 5432:5432 \
--name postgres-db \
postgres
```
#### 3. Create Pipenv & Install dependencies
```
pipenv shell
pip install -r requirements.txt
```

#### 4. Start app
`python url_shortener.py`

## Deploy in Docker
`docker-compose -f url_shortener.yml up`

## Deploy to EC2 in AWS
Generate an EC2 key pair called "main" and download the resulting .pem file.  

Generate Access Keys in AWS Console
```
export TF_VAR_access_key=<your-access-key>
export TF_VAR_secret_key=<your-secret-key>
```

From the Terraform directory run the following:
```
terraform init
terraform plan
terraform apply
```

SSH into the EC2 instance that is created, and run the following:
```
git clone https://github.com/jeff-vincent/url-shortener.git
cd url-shortener
sudo docker-compose -f url_shortener.yml up
```
