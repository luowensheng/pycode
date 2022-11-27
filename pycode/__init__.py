from tkwrapper import TkApp, TkFrame
from .main_menu import MainMenu
from .editor import Notebook




class Frame(TkFrame):
     notebook: Notebook()



class App(TkApp):
    menu: MainMenu()
    main_frame: Frame()
            