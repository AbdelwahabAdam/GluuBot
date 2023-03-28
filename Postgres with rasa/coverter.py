# ## ---------------------------------------------------------------- ##
# ## ----------------------- Convert JSON to YAML ------------------- ##
# ## ---------------------------------------------------------------- ##
import sys, io
import ruamel.yaml
import os 
import json

class MyConverter: 
    def __init__(self):
        self.yaml = ruamel.yaml.YAML()

    def literalize_list(self,v):
        assert isinstance(v, list)
        buf = io.StringIO()
        self.yaml.dump(v, buf)
        return ruamel.yaml.scalarstring.LiteralScalarString(buf.getvalue())

    def transform_value(self,d, key, transformation):
        """recursively walk over data structure to find key and apply transformation on the value"""
        if isinstance(d, dict):
            for k, v in d.items():
                if k == key:
                    d[k] = transformation(v)
                else:
                    self.transform_value(v, key, transformation)
        elif isinstance(d, list):
            for elem in d:
                self.transform_value(elem, key, transformation)
        
    def get_yaml(self,json_data,yaml_out):
            self.transform_value(json_data, 'examples', self.literalize_list)
            self.yaml.dump(json_data, yaml_out)

# conv=MyConverter()



# for f in os.listdir():

#     if f in ['FromDataBase']:
#         for json_file in os.listdir(f):
#             print(json_file)
#             if json_file in ['nlu.json']:#['nlu.json','rules.json']:
#                 with open(str(f)+'/'+str(json_file), 'r') as json_in, open('data/'+json_file.replace('json','yml'), "w") as yaml_out:
#                     json_data = json.load(json_in)
#                     conv.get_yaml(json_data,yaml_out)


# #             elif json_file in ['domain.json']:
# #                 with open(str(f)+'/'+str(json_file), 'r') as json_in, open(json_file.replace('json','yml'), "w") as yaml_out:
# #                     json_data = json.load(json_in)
# #                     transform_value(json_data, 'examples', literalize_list)
# #                     yaml.dump(json_data, yaml_out)