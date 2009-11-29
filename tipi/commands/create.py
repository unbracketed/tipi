from tipi.commands.base import LabelCommand

class Command(LabelCommand):
    help = "Creates a new virtualenv"

    def handle_label(self, label, **options):
        pass