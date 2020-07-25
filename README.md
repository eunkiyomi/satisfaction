# satisfaction
Bless you, my dear
[https://github.com/PPYAPgit/satisfaction]

> https://satisfaction-251312.du.r.appspot.com/

## How to edit
We should use *satisfaction-git* directory.

After edit, use
- `git add .`, then changed files will be tracked. (We can see this by `git status`)
- `git commit -m "<description>"`, then tracked files will be committed.
- `git push origin master`, then committed files will be saved in the master branch. (which is online.)

After push, go to server and
- `git pull origin master`, then files in server will be updated.

## Use Local Server
Run `runserver` in *satisfaction/manage.py*
- `python3 manage.py runserver`, then local server will run at port 8000.

## Clone it
```
$ git clone https://github.com/PPYAPgit/satisfaction
$ cd satisfaction/satisfaction
$ pip install -r requirements.txt`
$ python3 -m venv venv
$ source venv/bin/activate
$ python manage.py createsuperuser
$ python manage.py collectstatic
$ python manage.py runserver
```

## secrets.py
We should set `satisfaction/satisfaction/secrets.py` for some secret values
```
SECRET_KEY = "blahblah" # We can generate it at [https://djecrety.ir/]
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
```
## Apply Google OAuth API
We can follow this blog to apply *Login with Google*.
- [https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5]

## Using Google App Engine to deploy
- Install Google Cloud SDK [https://cloud.google.com/sdk/install]
```
$ gcloud init
```
- Follow this instruction [https://cloud.google.com/python/django/appengine]
```
$ cd satisfaction/satisfaction
$ gcloud services enable sqladmin
$ wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
$ chmod +x cloud_sql_proxy
```
- Create Cloud SQL instance
```
$ gcloud sql instances create satisfaction-instance --tier=db-n1-standard-2 --region=asia-northeast3
```
- Run Cloud proxy
```
$ gcloud sql instances describe satisfaction-instance
...
connectionName: [PROJECT_NAME]:[REGION_NAME]:satisfaction-instance 
...

$ ./cloud_sql_proxy -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:3306
```
- Create Cloud SQL User
```
$ gcloud sql databases create db --instance=satisfaction-instance 
$ gcloud sql users set-password root --host=% --instance=satisfaction-instance --prompt-for-password
$ gcloud sql users create satisfaction-user --host=localhost --instance=satisfaction-instance --password=[PASSWORD]
```
- Deploy
```
$ python manage.py migrate
$ python manage.py createsuperuser
$ cd [PROJECT ROOT]
$ gcloud app deploy
```