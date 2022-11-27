from tkwrapper import TkMenu, TkCommand, TkSeparator

class FileMenu(TkMenu):
    
    new_text_file: TkCommand()
    new_file: TkCommand()
    new_window: TkCommand()
    
    separator_1: TkSeparator()
    
    open_file: TkCommand()
    open_folder: TkCommand()
    open_workspace_from_file: TkCommand()
    open_recent: TkCommand()
    
    separator_2: TkSeparator()
    
    add_folder_to_workspace: TkCommand()
    save_workspace_as: TkCommand()
    duplicate_workspace: TkCommand()
    
    separator_3: TkSeparator()
    
    save: TkCommand()
    save_as: TkCommand()
    save_all: TkCommand()
    
    separator_4: TkSeparator()
    
    share: TkCommand()
    
    separator_5: TkSeparator()
    
    auto_save: TkCommand()
    preferences: TkCommand()
    
    separator_6: TkSeparator()
    
    revert_file: TkCommand()
    close_editor: TkCommand()
    close_window: TkCommand()
    
    separator_7: TkSeparator()
    
    exit: TkCommand()
    
    
    
    
    