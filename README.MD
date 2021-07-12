# **OOH** TV - Out Of Home TV

**Use the following websites to build the doc's diagrams:** [plantuml](https://plantuml.com) or [planttext](https://www.planttext.com).

**Install system dependenceis:**

```shell
# to install python
sudo apt install python3 python3-dev python3-pip python3-setuptools python3-wheel

# to get the PDF generetor working
sudo apt install texlive-latex-recommended texlive-lang-portuguese texlive-fonts-recommended

# to get the media import working
sudo apt install libmediainfo-dev
```
about [texliv](https://linuxconfig.org/how-to-install-latex-on-ubuntu-18-04-bionic-beaver-linux).

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

**To clean all migration files**

```find . -path "*/migrations/*.pyc"  -delete```
```find . -path "*/migrations/*.py" -not -name "__init__.py" -delete```

**To generate grpc code, if needed:**

_**NOTE:** This spet is not required if you only want to install and run the project_

```shell
cd oohtv/oohtv/grpc
python3 -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/rpcgate.proto
```
Them go the file **rpcgate_pb2_grpc.py** and change the line
```python
import rpcgate_pb2 as rpcgate__pb2
```
to
```python
from . import rpcgate_pb2 as rpcgate__pb2
```

**Finally run the project**

In one shell, raise the postgres and rabbitmq servers:

```shell
sudo docker-compose up
```

In another shell, configure the django server:

```shell
source .virenv/bin/activate
cd oohtv/

# construct the database
python manage.py migrate

# populate the database with important starter info
# in production
python manage.py populator
# in development
python manage.py populator -dev=true

# see: python manage.py populator -h
# for more info into this command:

# to run the development server
python manage.py runserver
```

In another shell, start grpc server:
```shell
source .virenv/bin/activate
cd oohtv/

# in production
python manage.py grpc -host=your_host -port=your_port
# in development
python manage.py grpc -insecure=true -debug=true

# see: python manage.py grpc -h
# for more info into this command
```

In another shell, start celery server:
```shell
source .virenv/bin/activate
cd oohtv/

watchmedo auto-restart --directory="./" --pattern="*.py" --recursive -- celery -A oohtv worker -l info --concurrency=2

# We still do not know how to put that in production .-.
```

<!-- psql baseTestForNewJob -h 127.0.0.1 -d newJobDB -f ./trash/script.sql
 -->
