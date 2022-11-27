from tkwrapper import TkMenu, TkCommand, TkSeparator

class GoMenu(TkMenu):
    
    back: TkCommand()
    forward: TkCommand()
    last_edit_location: TkCommand()
    
    separator_1: TkSeparator()
    
    switch_editor: TkCommand()
    switch_group: TkCommand()
    
    separator_2: TkSeparator()
    
    go_to_file: TkCommand()
    go_to_symbol_in_workspace: TkCommand()
    
    separator_3: TkSeparator()
    
    go_to_symbol_in_editor: TkCommand()
    go_to_definition: TkCommand()
    go_to_declaration: TkCommand()
    go_to_type_definition: TkCommand()
    go_to_implementations: TkCommand()
    go_to_references: TkCommand()
    
    separator_4: TkSeparator()
    
    go_to_line_comment: TkCommand(name="Go to Line/Column")
    go_to_bracket: TkCommand()
    
    separator_5: TkSeparator()
    
    next_problem: TkCommand()
    previous_problem: TkCommand()
    
    separator_6: TkSeparator()
    
    next_change: TkCommand()
    previous_change: TkCommand()
    
    
    
    
    