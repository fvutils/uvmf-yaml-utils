'''
Created on May 5, 2022

@author: mballance
'''

import uvmf_yaml_utils as uyu
from test_base import TestBase

class TestSmoke(TestBase):
    
    def test_smoke(self):
        
        env1 = self.createFile("env1.yaml", 
        """
        uvmf:
          environments:
            env1: {}
        """)
        
        print("path=%s" % env1)
        
        lib = uyu.Library()
        lib.addPath(env1)
        
        lib.load()
        
        for e in lib.getEnvironments():
            print("Environment: %s" % e.name)
            
        self.assertIsNotNone(lib.findEnvironment("env1"))
        
        e = lib.findEnvironment("env1")
        
        pass