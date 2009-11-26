import os
from unittest import TestCase

from tipi import create


class TipiAPITest(TestCase):
    
    def setUp(self):
        
        #create a temp VE home
        
        os.environ['TIPI_VENV_HOME'] = os.getcwd()
        
        pass
    
    def tearDown(self):
        #make sure all VEs are deleted
        pass
    
    def test_create(self):
        create()


class TipiCLITest(TestCase):
    pass



