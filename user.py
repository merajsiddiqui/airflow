import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user = PasswordUser(models.User())
user.username = 'meraj.siddiqui'
user.email = 'meraj.siddiqui@o4s.io'
user.password = 'meraj'
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()