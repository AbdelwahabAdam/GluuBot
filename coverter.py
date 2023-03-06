import yaml
import json
import os

cur_dir = os.getcwd()

for f in os.listdir():
    if f in ['data','domain']:
        for yml_file in os.listdir(f):
            if yml_file in ['nlu.yml','rules.yml','stories.yml','domain.yml']:
                with open(str(f)+'/'+str(yml_file), 'r') as yaml_in, open('json_data/'+yml_file.replace('yml','json'), "w") as json_out:
                    yaml_object = yaml.safe_load(yaml_in) 
                    json.dump(yaml_object, json_out)
