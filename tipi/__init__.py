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
        #import pdb; pdb.set_trace()
        commands = get_commands(__path__[0])
        commands.sort()
        for cmd in commands:
            usage.append('  %s' % cmd)
        return '\n'.join(usage)

    def fetch_command(self, subcommand):
        """
        Tries to fetch the given subcommand, printing a message with the
        appropriate command called from the command line (usually
        "django-admin.py" or "manage.py") if it can't be found.
        """
        try:
            app_name = get_commands()[subcommand]
            if isinstance(app_name, BaseCommand):
                # If the command is already loaded, use it directly.
                klass = app_name
            else:
                klass = load_command_class(app_name, subcommand)
        except KeyError:
            sys.stderr.write("Unknown command: %r\nType '%s help' for usage.\n" % \
                (subcommand, self.prog_name))
            sys.exit(1)
        return klass

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
            #handle_default_options(options)
            print options, args
        except:
            pass # Ignore any option errors at this point.

        try:
            subcommand = self.argv[1]
        except IndexError:
            sys.stderr.write("Type '%s help' for usage.\n" % self.prog_name)
            sys.exit(1)
        #import pdb; pdb.set_trace()
        if subcommand == 'help':
            if len(args) > 2:
                self.fetch_command(args[2]).print_help(self.prog_name, args[2])
            else:
                #parser.print_lax_help()
                parser.print_help()
                sys.stderr.write(self.main_help_text() + '\n')
                sys.exit(1)
        elif self.argv[1:] == ['--version']:
            print get_version()
            sys.exit(0)
        elif self.argv[1:] == ['--help']:
            sys.stderr.write(self.main_help_text() + '\n')
        else:
            self.fetch_command(subcommand).run_from_argv(self.argv)


#TODO placeholder
def get_version():
    return (0,1,0)


def get_commands(management_dir):
    """
    Returns a list of the Tipi commands
    """
    command_dir = os.path.join(management_dir, 'commands')
    try:
        return [f[:-3] for f in os.listdir(command_dir)
                            if not f.startswith('_') and \
                               not f.startswith('base') and \
                               f.endswith('.py')]
    except OSError:
        return []
            

def execute_from_command_line(argv=None):
    """
    A simple method that runs a CommandDispatcher.
    """
    dispatch = CommandDispatch(argv)
    dispatch.execute()




