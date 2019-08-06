# Airflow
Airflow Setting up dags and working with dag

## Installation 
```
virtualenv -p python3 venv
source venv/bin.activate
pip install -r requirements.txt
mkdir home
export AIRFLOW_HOME=`pwd`/home
```
## Configuration
When using mysql need to do one additinal setting

```
[mysqld]
explicit_defaults_for_timestamp = 1
```
for ubuntu `/etc/mysql/mysql.conf.d/mysqld.cnf`

Run command
```
airflow initdb
```
> once it returns `done` run command `airflow version` and it should list the version of airflow without any errors
