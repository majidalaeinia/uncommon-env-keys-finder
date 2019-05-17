#!/usr/bin/env python
env_file = '.env'
env_example_file = '.env.example'


def count_of_keys_available(file_name):
    """
    Count the number of non-blank and non-comment lines in a file.
    By comment, we mean the lines starting with '#'.

    :param file_name: string
    :return: int
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()
        count_of_lines_starting_with_a_key = len(
            [line for line in lines if (line.strip(' \n') != '' and line[0] != '#')])
        f.close()

        return count_of_lines_starting_with_a_key


def convert_each_file_line_to_a_list_item(file_name):
    """
    Convert each file line, into a list item.

    :param file_name:
    :return: list
    """
    try:
        with open(file_name) as the_file:
            the_file_lines = the_file.readlines()
            the_file.close()

        return the_file_lines

    except Exception as error:
        return error


def make_a_list_from_the_file_keys(file_name):
    """
    Make a list from the file keys.

    :param file_name:
    :return: list
    """
    try:
        the_file = []
        for line in convert_each_file_line_to_a_list_item(file_name):
            equal_index = line.find('=')
            file_key = line[:equal_index]
            the_file.append(file_key)

        return the_file

    except Exception as error:
        return error


def make_a_list_from_uncommon_items(list1, list2):
    """
    Make a list from uncommon items between two lists.

    :param list1:
    :param list2:
    :return: list
    """
    try:
        if len(list1) - len(list2) >= 0:
            return list(set(list1) - set(list2))

        return list(set(list2) - set(list1))

    except Exception as error:
        return error


if __name__ == '__main__':
    if len(make_a_list_from_uncommon_items(make_a_list_from_the_file_keys(env_file),
                                           make_a_list_from_the_file_keys(env_example_file))) == 0:
        print('The files have the same keys, no need to double check.')

    for item in make_a_list_from_uncommon_items(make_a_list_from_the_file_keys(env_file),
                                                make_a_list_from_the_file_keys(env_example_file)):
        print(item)
