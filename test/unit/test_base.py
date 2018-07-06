# -*- coding: utf-8 -*-
"""
unit tests
"""

# add parent folders to system path to import classes to testing
import sys
sys.path.append('../')

from test_conf import *

import law
import searcher
import search_master

class TestBotProcessor(object):
    """ Unit Tests for Processing Module
    """

    def test_search(self):
        test_searcher = searcher.Searcher('../state_data', 'new-jersey', '2015')
        legal_result = test_searcher.search_keyword('arson')[0]
        assert 'arson' in legal_result.text

        return
