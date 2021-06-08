import json
import os


dir = ['.', 'visualplotter', 'profiles'] 
path = os.path.join(*dir)

def read_config(file_name='Default_profile.json'):
    with open(os.path.join(path, file_name)) as json_file:
        config = json.load(json_file)
    return config

def write_config(file_name, config):
    with open(os.path.join(path, file_name), 'w') as json_file:
            json.dump(config, json_file, indent=4)
