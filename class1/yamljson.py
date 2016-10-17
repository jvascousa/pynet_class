#!/usr/bin/env python

import yaml
import json


def main():

    yaml_file = 'yaml_test.yaml'
    json_file = 'json_file.json'

    cisco_plat = {
        'ip_addr':'10.1.1.1',
        'vendor':'Cisco',
        'model':'7609',
        'Software':'IOS'}


    my_list=[range(8),cisco_plat,'some crazy','not sure what']

    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list,default_flow_style=False))
        #f.write(yaml.dump(my_list))

    with open(json_file, "w") as f:
        json.dump(my_list,f)

if __name__ == "__main__":
    main()
