import os
from subprocess import Popen, PIPE
from tempfile import mkdtemp
from unittest import TestCase

#from tipi.commands import creat


class TipiAPITest(TestCase):
    
    def setUp(self):
        #create a temp VE home
        self.ve_home = mkdtemp()
        os.environ['TIPI_VENV_HOME'] = self.ve_home
        
    def tearDown(self):
        #make sure all VEs are deleted
        os.rmdir(self.ve_home)
    
    def test_create(self):
        #verify created
        #verify it can be activated
        pass
    
    def test_create_name_clash_fails(self):
        pass
        
    

class TipiCLITest(TestCase):
    
    def setUp(TestCase):
        pass
    
    def runproc(self, *args):
        #print args
        return Popen(["tipi",] + list(args), stdout=PIPE, stderr=PIPE).communicate()
        
    def test_no_args(self):
        output, error = self.runproc()
        self.assertEqual("Type 'tipi help' for usage.", error.rstrip())
    
    def test_display_help(self):
        output, error = self.runproc('help')
        print "OUT: %s" % output
        print "ERROR: %s" % error
        self.assertEqual("\nType tipi help <subcommand>' for help on a specific subcommand.\n\nAvailable subcommands:\n  create\n  extend", error.rstrip())
        output, error = self.runproc('--help')
        print "OUT: %s" % output
        print "ERROR: %s" % error
        self.assertTrue(output.startswith('Usage:'))
            
    def test_display_version(self):
        output, error = self.runproc('--version')
        
        #TODO: placeholder
        self.assertEqual(str((0, 1, 0)),output.rstrip())

    def test_verbosity(self):
        #TODO
        pass
    
    def test_diplay_create_help(self):
        output, error = self.runproc('help','create')
        if not output.startswith('Usage: tipi create'):
            self.fail()
    
    def test_create_no_args(self):
        o,e = self.runproc('create')
        self.assertEqual(e.rstrip(),'Error: Enter at least one virtualenv name.')

    def test_virtualenv_options_passthrough(self):
        #TODO: make sure virtualenv options can be passed through
        pass
