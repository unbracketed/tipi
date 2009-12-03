"""
Runs Tipi commands. Handles presenting help text or identifying the requested
subcommand and invoking it with the arguments. Heavily inspired by the Django
management system.

"""
import os
import sys
from optparse import OptionParser

from tipi.commands.base import BaseCommand


class CommandDispatch(object):
    """
    Handles the initial parsing of the command line in order to determine
    which subcommand is being requested or to display appropriate help text.
    Passes off the remaining command line args to the Tipi command.
    
    """
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])

    def main_help_text(self):
        """
        Returns the script's main help text, as a string.
        """
        usage = ['',"Type %s help <subcommand>' for help on a specific subcommand." % self.prog_name,'']
        usage.append('Available subcommands:')
        
        commands = get_commands(__path__[0])
        commands.sort()
        for cmd in commands:
            usage.append('  %s' % cmd)
        return '\n'.join(usage)


    def execute(self):
        """
        Given the command-line arguments, this figures out which subcommand is
        being run, creates a parser appropriate to that command, and runs it.
        """
        
        parser = OptionParser(usage="%prog subcommand [options] [args]",
                                 version=get_version(),
                                 option_list=BaseCommand.option_list)
        try:
            options, args = parser.parse_args(self.argv)
        except:
            pass # Ignore any option errors at this point.

        try:
            subcommand = self.argv[1]
        except IndexError:
            sys.stderr.write("Type '%s help' for usage.\n" % self.prog_name)
            sys.exit(1)
        
        if subcommand == 'help':
            if len(args) > 2:
                get_command(args[2]).print_help(self.prog_name, args[2])
            else:
                parser.print_help()
                sys.stderr.write(self.main_help_text() + '\n')
                sys.exit(1)
        elif self.argv[1:] == ['--version']:
            print get_version()
            sys.exit(0)
        elif self.argv[1:] == ['--help']:
            sys.stderr.write(self.main_help_text() + '\n')
        else:
            get_command(subcommand).run_from_argv(self.argv)


#TODO placeholder
def get_version():
    return (0,1,0)


def get_commands(*args, **kwargs):
    """
    Returns a list of the Tipi commands
    """
    command_dir = os.path.join(__path__[0], 'commands')
    try:
        return [f[:-3] for f in os.listdir(command_dir)
                            if not f.startswith('_') and \
                               not f.startswith('base') and \
                               f.endswith('.py')]
    except OSError:
        return []
            

def get_command(name):
    cmd_path = 'tipi.commands.%s' % name
    __import__(cmd_path)
    command_module = sys.modules[cmd_path]
    klass = command_module.Command()
    return klass


def call_command(name, *args, **options):
    """
    Calls the given command, with the given options and args/kwargs.

    This is the primary API you should use for calling specific commands.

    Some examples:
        call_command('create', 'myenv')
        call_command('export', flat=True)
    """
    # Load the command object.
    try:
        #command exists?
        get_commands().index(name)
        klass = get_command(name)        
    except ValueError:
        raise CommandError, "Unknown command: %r" % name

    # Grab out a list of defaults from the options. optparse does this for us
    # when the script runs from the command line, but since call_command can
    # be called programatically, we need to simulate the loading and handling
    # of defaults (see #10080 for details).
    defaults = dict([(o.dest, o.default)
                     for o in klass.option_list
                     if o.default is not NO_DEFAULT])
    defaults.update(options)

    return klass.execute(*args, **defaults)


def execute_from_command_line(argv=None):
    """
    A simple method that runs a CommandDispatcher.
    """
    dispatch = CommandDispatch(argv)
    dispatch.execute()




