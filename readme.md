## Docker Compose for Rasa chatbot integrated with Postgres BD.

### This git repo contains the following
#### Directories
- FromDataBase
  - This directory contain the `JSON` data fetched from the Postgres DB.
- data_not_used
  - This directory contain the `yml` data that rasa uses by defult to train the bot, but we dont use it here (as we fetch data from DB).
- database
  - Thid directory contain `sql` file to create the `intent` table and add some inital data to it.
  - models
    - This directory will contain the training models data.
----------------
#### Files
- config.yml
  - This file contain the configuration for the bot (Custom importer).
- converter.py
  - This file contain the conversion script, that convert `Json` data from DB to `yml` data.
- custom_importer.py
  - This file contain the interface with the DB, converter, and rasa data.
- database_wrapper.py
  - This is a wrapper for DB, that contain some methods to fetch, add, edit on the DB.
- docker-compose.yml
  - This is the docker compose file, that contain all the services used.
- domain.yml
  - This file contain the intents and the responses for the bot.

----------------
## prerequisites.
you must have the following installed to test
- git
- docker
----------------
## In order to Test Using docker.
- Make new dir for the project
  >$ mkdir GluuBot
- Go to the new directory
  >$ cd  GluuBot
- Pull the repo using 
  >$ git pull https://github.com/AbdelwahabAdam/GluuBot.git
- Up the compose
  >$ docker-compose up -d
----------------
## In order to Test Without docker (UBUNTU).

- ### Install and init Rasa 
- ### Add the custom Importer 
- ### Edit the config file
- ### Setup Postgres
----------------

### To install Rasa on Ubuntu we should first install a modern python version.

- To install Rasa on Ubuntu we should first install a modern python version.


```sh
# First we should update apt, just in case.
sudo apt update
# Install python
sudo apt install python3-dev python3
# Once it is installed you should be able to confirm the versions.
python3 --version 
pip3 --version
```

- Now that we have these tools installed we can create a folder for our Rasa project.


```sh
# Create and Enter Folders
mkdir rasaprojects 
cd rasaprojects
# Next we install python3-pip so that we can install python packages
sudo apt install python3-venv
# We can now create a virtualenv 
python3 -m venv ./venv
```

- With our virtualenv available we can now active it and install Rasa.

```sh
# Source the virtualenv
source ./venv/bin/activate
# Install Rasa and Upgrade pip 
python -m pip install --upgrade pip rasa
# Our `python` now refers to the python version in the virtualenv.
# From here you should be able to use Rasa
python -m rasa --help
python -m rasa init
```

- Now we can use `rasa train` and `rasa shell`
  - `rasa train` will read the training data from `data` dir and `domain.yml` file, and then the training process starts.
  - `rasa shell` will open an interactive session in the shell to chat with the bot.
---------------
## Add the custom Importer in you rasa project directories
- Creat a new python file called `custom_importer.py`
- copy the content from same file from the git repo

---------------

## Add the Importer in the config file

- Open `config.yaml` and add the importer section
- The defult importer used with rasa is the `RasaFileImporter`

```yaml
importers:
- name: "RasaFileImporter"
```

- Add the Custom importer 

```yaml
importers:
- name: "custom_importer.MyImporter"
```

* NOTE
    - you can add the defult importer as well and rasa will combine the both, but Data directory must be there in your project dir.

```yaml
importers:
- name: "RasaFileImporter"
- name: "custom_importer.MyImporter"
  repository: "AbdelwahabAdam/hopa-rasa-demo"
```

#### OR
- simply replace the `config.yaml` in the repo with the one generated from `rasa init`.

-------
## Install Postgres

- Update packages list
  >$ sudo apt update
- Install postgres
  >$ apt install postgresql postgresql-contrib
- Check PostgreSQL status
  >$ service postgresql status
  - you should see `active`
  
## To train you bot from git data
- First call `rasa train`
- Then if every thing works well call `rasa shell` to test the bot in the terminal.

------