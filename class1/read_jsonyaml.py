#!/usr/bin/env python

import yaml
import json

from pprint import pprint


def output_print(my_list,my_str):
    print '\n\n'
    print '#' * 3
    print '#' * 3 + my_str
    print '#' * 3

    pprint(my_list)

def main():

    yaml_file = 'yaml_test.yaml'
    json_file = 'json_file.json'

    with open(yaml_file) as f:
        yaml_list = yaml.load(f)


    with open(json_file) as f:
        json_list = json.load(f)



    output_print(yaml_list,'YAML')
    output_print(json_list,'JSON')

if __name__ == "__main__":
    main()
