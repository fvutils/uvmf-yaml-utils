'''
Created on May 5, 2022

@author: mballance
'''
import os

from uvmf_yaml_utils.environment import Environment
from uvmf_yaml_utils.uvmf_core import yaml2uvmf


class Library(object):
    
    def __init__(self):
        self._path_l = []
        self._dc = None
    
    def addPath(self, path):
        self._path_l.append(path)
        
    def load(self):
        self._dc = yaml2uvmf.DataClass(None)
        
        for p in self._path_l:
            self._dc.parseFile(p)

        self._dc.validate()
    
    def getEnvironments(self):
        if self._dc is None:
            raise Exception("Library has not been loaded")
        
        ret = []
        for ename in self._dc.data['environments']:
            ret.append(Environment(ename, self._dc.data['environments'][ename]))
        return ret
    
    def findEnvironment(self, name):
        if self._dc is None:
            raise Exception("Library has not been loaded")
       
        if name in self._dc.data['environments']:
            return Environment(name, self._dc.data['environments'][name])
        else:
            return None
        