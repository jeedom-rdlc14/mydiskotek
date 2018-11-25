# myDiskoteK
myDiskoteK
flask-boostrap

A Flask app that can be used as a foundation for small projects (created initially by following [Mongo's Tumblelog tutorial](https://docs.mongodb.org/ecosystem/tutorial/write-a-tumblelog-application-with-flask-mongoengine/)).

[`flask-login`](https://github.com/maxcountryman/flask-login) was added to this project by following hints from [this article](https://runningcodes.net/flask-login-and-mongodb/).

Using:
* `flask`
* `flask-script`
* `WTForms`
* `mongoengine`
* `flask_mongoengine`
* `flask-login`

## Installation

The best way is to create a [`virtualenv`](http://virtualenv.org/) to isolate Python environments:
```
pip install virtualenv
virtualenv venv
```

Then, activate your `virtualenv` and install all the requirements:
```
source venv/bin/activate
pip install -r requirements.txt
```

If you've never worked with MongoDB before, here is a way to quickly get started with [Homebrew](http://brew.sh/):
```
brew update
brew install mongodb
sudo mkdir -p /data/db
sudo chown `id -u` /data/db
mongod
```

When you are done working with the project, deactivate the `virtualenv` (you can always re-activate later with `source venv/bin/activate`):
```
deactivate
```

## Run it!

Simples:
```
python manage.py runserver
```