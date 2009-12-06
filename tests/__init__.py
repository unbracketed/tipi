import os
from subprocess import Popen, PIPE
from tempfile import mkdtemp
from unittest import TestCase

#from tipi.commands import creat
from tipi import (execute_from_command_line, CommandDispatch, get_commands,
                  call_command,)
from tipi.commands.base import CommandError


class CommandRunner(object):
    """Utility class for invoking the command dispatcher"""
    
    def _d(self, *args):
        """Helper for dispatching commands"""
        print args
        cd = CommandDispatch(list(args))
        try:
            cd.execute()
        except SystemExit:
            pass
        
    def _cc(self, *args):
        try:
            call_command(*args)
        except SystemExit:
            pass


class TipiAPITest(TestCase, CommandRunner):
    
    def setUp(self):
        #create a temp VE home
        self.ve_home = mkdtemp()
        os.environ['TIPI_VENV_HOME'] = self.ve_home
        
    def tearDown(self):
        #make sure all VEs are deleted
        os.rmdir(self.ve_home)
        
    def test_bogus_command(self):
        
        self.assertRaises(CommandError, self._cc, 'bogus')
        
    def test_create(self):
        #verify created
        #verify it can be activated
        
        self._cc('create')
    
    def test_create_name_clash_fails(self):
        pass
    
    def test_fail_finding_commands(self):
        import tipi
        old_path = tipi.__path__
        tipi.__path__ = 'bogus'
        self.assertEqual(get_commands(), [])
        tipi.__path__ = old_path
        
        

    
    
class CommandDispatcherTest(TestCase, CommandRunner):
    """Tests commands and their options by invoking them through the
    CommandDispatch.
    
    """
    def test_execute_from_cl(self):
        try:
            execute_from_command_line(['tipi'])
        except SystemExit:
            pass
        
    def test_command_dispatch(self):
        
        self._d('tipi')
        self._d('tipi','help')
        self._d('tipi', 'help', 'create')
        self._d('tipi', '--version')
        
        cd = CommandDispatch(['tipi', 'help'])
        #TODO check output
        cd.main_help_text()
        
    def test_ambiguous_option(self):
        #TODO check output
        self._d('tipi','--bogus')
      

class TipiCLITest(TestCase, CommandRunner):
    """Test the commands by simulating invoking them from the command line"""
    
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
        self.assertEqual("\nType tipi help <subcommand>' for help on a specific subcommand.\n\nAvailable subcommands:\n  create\n  extend", error.rstrip())
        output, error = self.runproc('--help')
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
        
        #cover the command dispatcher subcommand
        self._d('tipi','create')

    def test_virtualenv_options_passthrough(self):
        #TODO: make sure virtualenv options can be passed through
        pass
