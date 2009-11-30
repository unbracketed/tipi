import subprocess
from tipi.commands.base import LabelCommand

class Command(LabelCommand):
    help = "Creates a new virtualenv"
    args = "[virtualenv_name]"
    label = "virtualenv name"

    def handle_label(self, label, **options):
        #TODO make sure ve with identical name doesn't exist
        subprocess.call(['virtualenv', label])
        