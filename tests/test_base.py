'''
Created on May 5, 2022

@author: mballance
'''
import os
from unittest.case import TestCase
import tempfile
import shutil

class TestBase(TestCase):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self._tmpdir = None
        
    def setUp(self):
        TestCase.setUp(self)
        self._tmpdir = tempfile.mkdtemp()
        
    def tearDown(self):
        TestCase.tearDown(self)
        shutil.rmtree(self._tmpdir)
        
    def createFile(self, path, content):
        dstpath = os.path.join(self._tmpdir, path)
        dstdir = os.path.dirname(dstpath)
        
        if not os.path.isdir(dstdir):
            os.makedirs(dstdir)
            
        with open(dstpath, "w") as fp:
            fp.write(content)
        
        return dstpath
        