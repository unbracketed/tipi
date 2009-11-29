import os
from tempfile import mkdtemp
from unittest import TestCase

from tipi import create


class TipiAPITest(TestCase):
    
    def setUp(self):
        #create a temp VE home
        self.ve_home = mkdtemp()
        os.environ['TIPI_VENV_HOME'] = self.ve_home
        
    def tearDown(self):
        #make sure all VEs are deleted
        os.rmdir(self.ve_home)
    
    def test_create(self):
        create()
        
    

class TipiCLITest(TestCase):
    
    def test_display_help(self):
        pass
    
    def test_display_version(self):
        pass


if __name__ == '__main__':
    
