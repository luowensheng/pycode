from tkwrapper import TkMenu, TkCommand, TkSeparator

class ViewMenu(TkMenu):
    
    command_palette: TkCommand()
    open_view: TkCommand()
    
    separator_1: TkSeparator()
    
    appearance: TkCommand()
    editor_layout: TkCommand()
    
    separator_2: TkSeparator()
    
    explorer: TkCommand()
    search: TkCommand()
    source_control: TkCommand()
    run: TkCommand()
    extensions: TkCommand()
    testing: TkCommand()
    
    separator_3: TkSeparator()
    
    problems: TkCommand()
    output: TkCommand()
    debug_console: TkCommand()
    terminal: TkCommand()
    
    separator_4: TkSeparator()
    
    word_wrap: TkCommand()
    sticky_scroll: TkCommand()
    