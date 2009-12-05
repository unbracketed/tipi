import os
import subprocess
from tipi.commands.base import LabelCommand

class Command(LabelCommand):
    help = "Creates a new virtualenv"
    args = "[virtualenv_name]"
    label = "virtualenv name"

    def handle_label(self, label, **options):
        #TODO make sure ve with identical name doesn't exist
        
        call_args = ['virtualenv', label, '--no-site-packages']
        if options.get('python'):
            call_args += ['--python', options['python']]
            
        #TODO: map verbose onto virtualenv verbose option
        #TODO: check for directory option
        #TODO: check for VENV_HOME or WORKON_HOME
        
        #TODO honor TIPI_VENV_HOME if it exists
        if 'TIPI_VENV_HOME' in os.environ:
            os.chdir(os.environ['TIPI_VENV_HOME'])
        
        subprocess.call(['virtualenv', label])
        
