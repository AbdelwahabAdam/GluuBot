## Docker Compose for Rasa chatbot integrated with Postgres BD.

### This git repo contains the following
#### Directories

- Postgres with rasa 
  - This dirctory contain all files to integrate rasa chatbot with posgtres, and let rasa fetch training data from the DB.

- Rocketchat with rasa
  - This dirctory contain all files to integrate rasa chatbot with Rocketchat, This use Omnichannel and Livechat features.

------------------
------------------
## First 
### Postgres with rasa
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
- db_command.py
  - This file handel the database. (add, update, delete, getValue, get)
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

## db_command.py

You can use this file to manpulate the database.
- `get`: to get all data in the DB
  > ex: python3 db_command.py get
- `add`: to add a new values
  > ex: python3 db_command.py add id intent_name ['intent','example'] responce
- `update`: to update certain value
  > ex: python3 db_command.py update response Bye! id 1
- `getValue`: to get certain value
  > ex: python3 db_command.py get_Value response id 1
- `delete`: to delete a row (on id)
  > ex: python3 db_command.py delete 1

------
## Install RocketChat service.
RocketChat service can installed using the following command:
  > sudo snap install rocketchat-server

also, we can Manage the RocketChat service using the following:
  > systemctl status `snap.rocketchat-server.rocketchat-server.service`

The MongoDB that powers the RocketChat server is ran by the 
`snap.rocketchat-server.rocketchat-mongo.service`

we can use all systemctl commands with it.

------------------
------------------
## Sec. 
### Postgres with rasa
#### Directories
- bot_rasa
  - This directory contain all training data for rasa chatbot.

----------------
#### Files
- docker-compose.yml
  - This is the docker compose file, that contain all the services used.
- redirectServer.py
  - This file creat a intermediary server that recieve from Rasa App in rocket and send it to rasa server and then revice from rasa server and sent the responce back to Rasa App in rocket.

----------------

## Rocketchat with rasa

There are several method to integrate both.
the best way using the rasa app from rocketchat market.

------

### Installation steps:


### Rocket Chat Setup

- create a new user. `Setting` > `Users`
- This new user must have these 2 roles.
    1. bot
    2. livechat-agent
- enable Omnichannel.
  -`Administration` > `workspace` > `setting` > `Omnichannel` > `Omnichannel enabled`

- Assign new conversations to bot agent.
-`Administration` > `workspace` > `setting` > `Omnichannel`  > `Routing` > `Assign new conversations to bot agent`
------

### Setup Rocket chat Omnichannel

- Add the bot to `Agents` 
  - `Administration` > `Omnichannel` > `Agents` > `add`
- Add new `Department`
  - add department with the name **`general`**

-------
### Rasa App setup
- Download directly from Rocket.Chat marketplace
- Fill neccessary fields in `Setting`
  - Bot Username (required)
    - the bot user name we created.
  - Rasa Server Url (required)
    - The URL for rasa server, here we will put another url for a python flask server. >> will be demonstrated later.
    - ex: http://**ip**:4000 >> put you device ip, dont put localhost
  - Default Handover Department Name (required)
    - add `general` that we created before.

------
### Note

- There is an error in the Rasa App, it sends data that rasa server couldn’t parse

EX:
- data that was sent by rasa app in rocket market >> single quotes
```
[{'recipient_id': 'default', 'text': 'Hey! How are you?'}]
```
- using postman to check, this body was parsed successfully >> double quotes
  
```
{
    "sender": "WMXQiQaQkxeTNLa2G", 
    "message": "hi"
}
```

- this body was failed >> single quotes
```
{
    'sender': 'WMXQiQaQkxeTNLa2G', 
    'message': 'hi'
}
```

we make a turnaround with python flask to receive it and send it back with double quotes. >> `redirectServer.py`


------
### How to test

- run the docker-compose.
- Follow the steps in `Rocket Chat Setup`.
- Follow the steps in `Setup Rocket chat Omnichannel`.
- Follow the steps in `Rasa App setup`.
- Run `redirectServer.py` server.
- open `localhost:3000/livechat`, choose department, then start.
- The livechat will start with rasa bot as Agent.
- Any message sent will be send to `rocketchat app` > then it will be sent to `Flask server` > then it will be formated and sent back to `Rocket chat rasa app` again.