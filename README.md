# universe


### Installation
- Preparation
```shell
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
```
- Install PostgreSQL
```shell
sudo apt install postgresql postgresql-contrib
```
- Create database and user
```shell
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
```
- Create a virtual environment
```shell
sudo apt install python3-venv
python3 -m venv venv
```
- Activate it
```shell
source venv/bin/activate
```
- Install dependencies
```shell
pip install -r requirements.txt
```
