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

## Authentication to enable password on UI
set  in `airflow.cfg`
```
[webserver]
authenticate = True
auth_backend = airflow.contrib.auth.backends.password_auth
```

Creating Super user
1. The first user can only be created by script
2. In the user.py file change the user credential
then run the command
```
python user.py
```

There are three parts 
1. Webserver
2. Scheduler
3. Worker

Webserver is responsible for web ui to access airflow UI to see logs and every opther things

Scheduer basically schedules the job to be process, If the configuration is ok then it will schedule the job

Worker is responsible for completing the job which will execute the job

If you want to access Web UI run command `airflow webserver`
in another terminal run `airflow scheduler` which will basicallsy schedule the job
Then in another terminal run `airflow worker` which will execute the job

