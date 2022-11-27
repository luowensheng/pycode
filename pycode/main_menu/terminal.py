from tkwrapper import TkMenu, TkCommand, TkSeparator

class TerminalMenu(TkMenu):
    
    new_terminal: TkCommand()
    split_terminal: TkCommand()
    
    separator_1: TkSeparator()
    
    run_task: TkCommand()
    run_build_task: TkCommand()
    run_active_file: TkCommand()
    run_selected_text: TkCommand()
    
    separator_2: TkSeparator()
    
    show_running_task: TkCommand()
    restart_running_task: TkCommand()
    terminate_task: TkCommand()
    
    separator_3: TkSeparator()
    
    configure_task: TkCommand()
    configure_default_build_task: TkCommand()
    
    
    
    
    