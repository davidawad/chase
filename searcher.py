#!/usr/bin/env python

"""
This class exposes functions to enable easy access to a
statedb formatted json file.
See statedb here: github.com/davidawad/statedb

 usage:
     g = search_keyword('arson')
     returns law objects
"""

import os
import json

import law


class Searcher:
    """
    tracks a json file in memory and searches it on demand
    """

    def __init__(self, directory: str, state: str, year: str):
        """
        Create our object, determine filepath and
        initialize information for searcher
        Args:
            directory (str): Directory that the file is in, such as 'state_data'
            state (str): state that the searcher is responsible for
            year (str): year that the searcher has on this state
        """

        self.state = state
        self.year = year
        # here, LEGAL_DATA is a string containing our json file
        self.LEGAL_DATA = None

        # naming convention is state_year
        self.LEGAL_DATA_FILENAME = './' + directory + '/' + state + '_' + year + '.json'

    def __str__(self):
        """
        string method for simplicity
        """
        return str(self.__dict__)

    def __eq__(self, other):
        """
        enables userA == userB
        """
        return self.__dict__ == other.__dict__

    # function to return legal data object
    def _fetch_data(self):
        """
        checks if json object has been read into memory
        and then returns it
        """

        if not self.LEGAL_DATA:
            with open(self.LEGAL_DATA_FILENAME) as f:
                self.LEGAL_DATA = json.load(f)

        return self.LEGAL_DATA

    # search the state code for a particular term and bring up all legal citations
    def search_keyword(self, keyword: str):
        """
        takes a keyword argument and send
        """
        if not keyword:
            return ''
        ret = self._search_nested_dict(keyword, self._fetch_data())
        return ret

    def available(self):
        """
        public sanity check that this object actually can reach the file it's supposed to
        """
        return os.path.exists(self.LEGAL_DATA_FILENAME)

    # search our legal data
    def _search_nested_dict(self, keyword, data=None, final_list=None):
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
                        # bundle = (citation, s)
                        current_law = law.Law(self.state, citation, s)

                        final_list.append(current_law)

            else:
                for key, val in data.items():
                    if key == 'link':
                        continue
                    self._search_nested_dict(keyword, val, final_list)

        # val is an array of objects
        elif isinstance(data, list):

            # recursively call on each object in val
            for index, val in enumerate(data):
                self._search_nested_dict(keyword, data[index], final_list)

        return final_list
