'''
Created on May 5, 2022

@author: mballance
'''

class Environment(object):
    
    def __init__(self, name, data):
        self._name = name
        self._data = data
        
    @property
    def name(self):
        return self._name
