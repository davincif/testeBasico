# **Test Job** - The Test for the New Job

**Install system dependenceis:**

```shell
# to install python
sudo apt install python3 python3-dev python3-pip python3-setuptools python3-wheel
```

**Install project dependenceis:**

_**NOTE:** The use of the **dependencymanager** package **isn't recommended in production**, it doesn't add much to that scenario anyway. Even though **it's strongly recommended for development**, 'cause that's precisely what maintain the development packages away from production._

```shell
virtualenv --python=python3 .virenv
source .virenv/bin/activate


# FOR DEPLOYMENT

# using only pip
pip install -r requirements.txt

# using dependencymanager
pip install dependencymanager
python -m dependencymanager install


# FOR DEVELOPMENT

# using only pip
pip install -r requirements.txt
pip install -r dev_requirements.txt

# using dependencymanager
pip install dependencymanager
python -m dependencymanager install --dev=true

```

**To format to pep8 standard code style**

```autopep8 --in-place --aggressive --aggressive --recursive ./```

**Run the project**

In one shell, raise the postgres and rabbitmq servers:

```shell
sudo docker-compose up
```

In another shell, configure the django server:

```shell
source .virenv/bin/activate

# construct the database
python manage.py migrate

# see: python manage.py populator -h
# for more info into this command:

# to run the development server
python manage.py runserver
```

<!-- psql baseTestForNewJob -h 127.0.0.1 -d newJobDB -f ./trash/script.sql
 -->
