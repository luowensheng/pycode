from tkwrapper import TkNotebook, TkFrame, TkText

class Editor(TkText):
    pass


class NotebookFrame(TkFrame):
    editor: Editor()


class Notebook(TkNotebook):
    frame: NotebookFrame(background_color="#2a2a2b")