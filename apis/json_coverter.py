## ---------------------------------------------------------------- ##
## ----------------------- Convert JSON to YAML ------------------- ##
## ---------------------------------------------------------------- ##
import yaml
import json
import os

cur_dir = os.getcwd()

for f in os.listdir():
    if f in ['json_data']:
        for json_file in os.listdir(f):
            if json_file in ['nlu.json','rules.json','stories.json']:
                with open(str(f)+'/'+str(json_file), 'r') as json_in, open('data/'+json_file.replace('json','yml'), "w") as yaml_out:
                    json_data = json.load(json_in)
                    yaml.dump(json_data,yaml_out,default_flow_style=False, sort_keys=False)
            elif json_file in ['domain.json']:
                with open(str(f)+'/'+str(json_file), 'r') as json_in, open('domain/'+json_file.replace('json','yml'), "w") as yaml_out:
                    json_data = json.load(json_in)
                    yaml.dump(json_data,yaml_out,default_flow_style=False, sort_keys=False)