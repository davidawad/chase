#!/usr/bin/python

"""
lightweight law container


each law object contains:
    raw text
    citation
    state
"""


class Law:

    def __init__(self, state: str, citation: str, text: str):
        """
        setup
        """
        self.state = state
        self.text = text
        self.citation = citation

    def __str__(self):
        """
        string method for simplicity
        """
        return str(self.__dict__)

    def __eq__(self, other):
        """
        enables lawA == lawB
        """
        return self.__dict__ == other.__dict__



