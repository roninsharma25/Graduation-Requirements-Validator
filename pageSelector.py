import streamlit as st

# Reference: https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030

class PageSelector():

    def __init__(self):
        # initialize pages
        self.pages = []
    
    def createPage(self, title, func):
        self.pages.append( { 'title': title, 'function': func } )

    def setPage(self, pageIndex):
        self.pages[pageIndex]['function']()