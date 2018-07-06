#!/bin/env/python

"""
Object to manage the searchers for the various states
"""

import os
from collections import defaultdict


import utils
import searcher


class SearchMaster:
    """
    organizes searcher classes
    """

    def __init__(self, directory: str):
        """
        setup

        on init looks though directory of laws and constructs
        nested searcher dictionary

        """
        # state_mapping = utils.state_name_map()

        self.available_searchers = defaultdict(dict)

        # on init, go through every item in folder and update dict accordingly
        for filename in os.listdir(directory):
            state, year = utils.state_file_info(filename)

            # create a searcher for this specific json file
            consumer_searcher = searcher.Searcher(directory, state, year)
            self.available_searchers[state][year] = consumer_searcher

    def search(self, query, state, year='2017'):
        """
        performs a search for the associated query
        year defaults if not defined

        query: arson
        state: NJ
        year : 2015
        """
        if not query or not state:
            return None

        state_key = utils.map_abbrev_to_state_key(state)

        searchers_for_state = self.available_searchers.get(state_key, False)

        if not searchers_for_state:
            return "No searcher available for that state."

        search_years = map(int, list(searchers_for_state.keys()))

        # find numerically closest year that's defined
        numerically_closest_year = str(min(search_years, key=lambda x: abs(x - int(year))))

        searcher_for_request = searchers_for_state[numerically_closest_year]

        return searcher_for_request.search_keyword(query)


