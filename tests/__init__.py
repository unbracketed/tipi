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
    
    def runproc(self, *args):
        print args
        return Popen(["tipi",] + list(args), stdout=PIPE, stderr=PIPE).communicate()
        
    def test_no_args(self):
        output, error = self.runproc()
        self.assertEqual("Type 'tipi help' for usage.", error.rstrip())
    
    def test_display_help(self):
        output, error = self.runproc('help')
        self.assertEqual("\nType tipi help <subcommand>' for help on a specific subcommand.\n\nAvailable subcommands:\n  create", error.rstrip())
        output, error = self.runproc('--help')
        self.assertEqual("\nType tipi help <subcommand>' for help on a specific subcommand.\n\nAvailable subcommands:\n  create", error.rstrip())
        
    
    def test_display_version(self):
        output, error = self.runproc('--version')
        #TODO: placeholder
        self.assertEqual(str((0,1,0,)),output.rstrip())



    
