import os
from subprocess import Popen, PIPE
from tempfile import mkdtemp
from unittest import TestCase

#rom tipi import create


class TipiAPITest(TestCase):
    
    def setUp(self):
        #create a temp VE home
        self.ve_home = mkdtemp()
        os.environ['TIPI_VENV_HOME'] = self.ve_home
        
    def tearDown(self):
        #make sure all VEs are deleted
        os.rmdir(self.ve_home)
    
    def test_create(self):
        #create()
        pass
        
    

class TipiCLITest(TestCase):
    
    def setUp(TestCase):
        pass
    
    
    def test_no_args(self):
        output, error = Popen(["tipi",], stdout=PIPE, stderr=PIPE).communicate()
        #print "OUTPUT IS %s" % output
        #print "ERROR IS %s" % error
        self.assertEqual("Type 'tipi help' for usage.", error.rstrip())
    
    def test_display_help(self):
        #subprocess.call()
        pass
    
    def test_display_version(self):
        pass



    
