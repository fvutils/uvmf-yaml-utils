'''
Created on May 17, 2022

@author: mballance
'''

class GenSpec(object):
    
    def __init__(self,
                 template_path=None,
                 outdir=None):
        self._template_path = template_path
        self._outdir = outdir
        
    @property
    def template_path(self):
        return self._template_path
    
    @property
    def outdir(self):
        return self._outdir
    
    
    
        
    