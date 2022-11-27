from tkwrapper import TkMenu, TkCommand, TkSeparator

class EditMenu(TkMenu):
    
    undo: TkCommand()
    redo: TkCommand()
    
    separator_1: TkSeparator()
    
    cut: TkCommand()
    copy: TkCommand()
    paste: TkCommand()
    
    separator_2: TkSeparator()
    
    find: TkCommand()
    replace: TkCommand()
    
    separator_3: TkSeparator()
    
    find_in_files: TkCommand()
    replace_in_files: TkCommand()
    
    separator_4: TkSeparator()
    
    toggle_line_comment: TkCommand()
    toggle_break_comment: TkCommand()
    emmet_expand_abreviration: TkCommand(name="Emmet: Expand Abbreviation")
    
    
    
    
    
    