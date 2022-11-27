from tkwrapper import TkMenu
from .file import FileMenu
from .edit import EditMenu
from .selection import SelectionMenu
from .view import ViewMenu
from .go import GoMenu
from .run import RunMenu
from .terminal import TerminalMenu
from .help import HelpMenu

class MainMenu(TkMenu):
    file: FileMenu(background_color="white")
    edit: EditMenu(background_color="white")
    selection: SelectionMenu(background_color="white")
    view: ViewMenu(background_color="white")
    go: GoMenu(background_color="white")
    run: RunMenu(background_color="white")
    terminal: TerminalMenu(background_color="white")
    help: HelpMenu(background_color="white")
