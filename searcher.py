#!/usr/bin/env python
"""This script exposes functions to enable easy access to a
statedb formatted json file.
See statedb here: github.com/davidawad/statedb"""

import json


# usage:
#     g = search_keyword('arson')
#     print(g[0][0], g[0][1])


SEARCH_ENDPOINT = "search"
STATE = "new-jersey"
YEAR = "2015"

LEGAL_DATA_FILENAME = 'state_data/' + STATE + '_' + YEAR + '.json'

# cache our data file locally so that we only load it once
LEGAL_DATA = None


# function to return legal data object
def fetch_data():
    """
    checks if json object has been read into memory
    and then returns it
    """
    ret = None

    global LEGAL_DATA

    if not LEGAL_DATA:
        with open(LEGAL_DATA_FILENAME) as f:
            LEGAL_DATA = json.load(f)

    ret = LEGAL_DATA

    return ret


# search the state code for a particular term and bring up all legal citations
def search_keyword(keyword):
    """
    takes a keyword argument and send
    """
    if not keyword:
        return ''
    ret = _search_nested_dict(keyword, fetch_data())
    return ret


# search our legal data
def _search_nested_dict(keyword, data=LEGAL_DATA, final_list=None):
    """
    Hacky graph-like traversal through this massive json object to
    find laws containing the specific keywords we might be interested in.
    """

    if final_list is None:
        final_list = []

    # data is null or empty, no reason
    if data is None:
        raise ValueError('Search provided with no data, \
                         is the state data being loaded properly?')

    # val is a dict
    if isinstance(data, dict):

        # if a 'raws' key is defined, we're at a leaf node and can examine it.
        if data.get('raws', False):

            arr = data.get('raws')

            for s in arr:
                # very loose check for relevance
                # this law contains the word we care about
                if keyword in s:
                    # find the title tag of our leaf node
                    # a key such as "section" or "title", etc.
                    unique_keys = [x for x in data.keys() if x not in ['link', 'raws']]

                    # the object title is going to be the tag that isn't link
                    # or raws
                    obj_title = unique_keys[0]

                    # title like the following :
                    # 'Section 1:1-1 - General rules of construction'
                    reference_title = data.get(obj_title)

                    # split it into 'Section 1:1-1'
                    citation = ' '.join(reference_title.split(" ")[0:2])

                    # add this citation to our list of legal occurrences
                    bundle = (citation, s)
                    final_list.append(bundle)

        else:
            for key, val in data.items():
                if key == 'link':
                    continue
                _search_nested_dict(keyword, val, final_list)

    # val is an array of objects
    elif isinstance(data, list):

        # recursively call on each object in val
        for index, val in enumerate(data):
            _search_nested_dict(keyword, data[index], final_list)

    return final_list


def clean_legal_text(uncleaned_text):
    """
    Some of the strings in the data contain newline characters that
    we don't want.
    This function just cleans up some of the cruft.
    """
    ret = uncleaned_text.replace("\n", " ")
    return ret



