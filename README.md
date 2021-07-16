# **Test Job** - A Test for the New Job

**Install system dependenceis:**

```sh
# to install python
sudo apt install python3 python3-dev python3-pip python3-setuptools python3-wheel
```

**Install project dependenceis:**

_**NOTE:** The use of the **dependencymanager** package is **not recommended in production**. However it's strongly **recommended for development**, 'cause that's precisely what maintains the development packages away from production._

```sh
virtualenv --python=python3.8 .virenv
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

**Run the project**

In one shell, raise the dockerzied Postgres server:

```sh
sudo docker-compose up
```

In another shell, configure the django server:

```sh
source .virenv/bin/activate

# construct the database
python manage.py migrate

# to run the development server
python manage.py runserver
```

## Envolved Technologies

* Django 3
* Jquery
* Vue.js
* Bootstrap 5
* GIT

## Why These Technologies?

Although I have much more experience making front-ends in SPA's (Single Page Applications) frameworks like Angular and specially React, I judged that separating front-end and back-end could be unfeasible for me, given that I'm having **problems with my computer** and, more importantly, the **time** per day I had to dedicate to the project.

* **Django** is a very well consolidate technology, with almost 10 years in the merkat and being used by complanies like globo.com to this day (see [here](https://python.org.br/empresas/)). It would hold most of the font/back interactions and I could write in Python, a language that I considerabely like. Basically making it unnecessary for me to deal with a REST API and use only vanilla HTML to build everything.

    The **desvantage** of this approach is that Django has a known problem: dealing with dinamic content in the screen. That's one of the reasons why SAP's frameworks exists to begin with.

* So **Vue.js** comes in handy here. I needed very few dinamic interactions in the web site, so nothing better than a light weight, with almost no settup requeried to work, and easy framwork: _vue.js_. Note that it's not the entire Vue framework, I'm not using the cli and all that (like [that](https://vuejs.org/v2/guide/)). only it's _js_ file injected directly in the html, making it possible to build not only SPA's.

* **Jquery** was only used to make it easier to make some queries to the html, pretty standard use.

* **Bootstrap**, well... I'm very bad at web design, I usually implement someone else's design, which is a pretty normal development pipe in the industry. So I was expecting already that my website would look bad and with horrible taste for colors :man_facepalming:. Therefore using Bootstrap would not only speed up my styling, but it's also the only hope that I wouldn't look border line unprofessional with my design.

* **GIT** to avoid unecessary losses. ^^" I make use of the rebasing then mergin with FF (Fast-Forward) technic, that's why there's no merge msg in the commits or things of the sort. But yes I craeted branches for each task, then rebased, merged and deleted.

## About the Extra Points for the Project
In the _Extra points_ section I'm asked to say what's missing in the SQL script. And although my knowledges about pure SQL are rusty, I think I can give it a go:

* **SALA** - It's missing to add the **CONSTRAIN** to **PRIMARY KEY** in the **ID** fild.

* **PROFESSOR** - Missing THE **CONSTRAIN** to **FOREING KEY** in the **ID_SALA** fild.

* **ALUNO** - Missing THE **CONSTRAIN** to **FOREING KEY** in the **ID_PROFESSOR** fild. Also, as Stundents must have a teacher it's also missing to add **NOT NULL** to the field above mentioned.

* **EXTRA** - All in all, in **PROFESSOR** and **ALUNO** I would consider the use of the statement **CASCADE** to garantee the correctness and consitency of the data base over time.

<!-- psql baseTestForNewJob -h 127.0.0.1 -d newJobDB -f ./trash/script.sql
 -->
