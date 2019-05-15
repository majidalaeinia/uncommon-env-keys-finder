#!/usr/bin/env python
from functions_module import *

env_file = 'env.txt'
env_example_file = 'env_example.txt'

if __name__ == '__main__':
    if len(make_a_list_from_uncommon_items(make_a_list_from_the_file_keys(env_file),
                                           make_a_list_from_the_file_keys(env_example_file))) == 0:
        print('The files have the same keys, no need to double check.')

    for item in make_a_list_from_uncommon_items(make_a_list_from_the_file_keys(env_file),
                                                make_a_list_from_the_file_keys(env_example_file)):
        print(item)
