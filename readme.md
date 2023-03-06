## This is a smiple test for Custom importer to get training data from github

- This git repo contain the Training data (nlu.yml,stories.yml,rules.yml)

- The Custom importer script (custom_importer.py)

- The configuration file (config.yaml)

----------------
## In order to Test the Importer
- Install and init Rasa 
- Add the custom Importer in you rasa project directories
- Add the Importer in the config file

-------------------

## Install and init Rasa 

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

- Add the Custom importer and add a `repository` parametar (one indent) 

- But there the git repo name in this case the repo name is `AbdelwahabAdam/hopa-rasa-demo`

```yaml
importers:
- name: "custom_importer.MyImporter"
  repository: "AbdelwahabAdam/hopa-rasa-demo"
```

* NOTE
    - you can add the defult importer as well and rasa will combine the both, but Data directory must be there in your project dir.

```yaml
importers:
- name: "RasaFileImporter"
- name: "custom_importer.MyImporter"
  repository: "AbdelwahabAdam/hopa-rasa-demo"
```

-------

# To tran you bot from git data
- First call `rasa train`
- Then if every thing works well call `rasa shell` to test the bot in the terminal