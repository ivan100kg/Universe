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
sudo -u postgres psql
```
- Create database and user
```shell
CREATE DATABASE universe;
CREATE USER spaceman WITH PASSWORD '12345';
ALTER ROLE spaceman SET client_encoding TO 'utf8';
ALTER ROLE spaceman SET default_transaction_isolation TO 'read committed';
ALTER ROLE spaceman SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE universe TO spaceman;
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
