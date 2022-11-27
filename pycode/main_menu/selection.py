from tkwrapper import TkMenu, TkCommand, TkSeparator

class SelectionMenu(TkMenu):
    
    select_all: TkCommand()
    expand_selection: TkCommand()
    shrink_selection: TkCommand()
    
    separator_1: TkSeparator()
    
    copy_line_up: TkCommand()
    copy_line_down: TkCommand()
    move_line_up: TkCommand()
    move_line_down: TkCommand()
    duplicate_selection: TkCommand()
    
    separator_2: TkSeparator()
    
    add_cursor_above: TkCommand()
    add_cursor_below: TkCommand()
    add_cursor_to_line_ends: TkCommand()
    add_next_occurrence: TkCommand()
    add_previous_occurrence: TkCommand()
    select_all_occurrences: TkCommand()
    
    separator_3: TkSeparator()
    
    multi_cursor: TkCommand(name="Switch to Ctrl+Click for Multi-Cursor")
    column_selection_mode: TkCommand()
    
    
    
    
    
    