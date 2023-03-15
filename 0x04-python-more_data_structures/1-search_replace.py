#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    return [replace if item == search else item for item in new]
