from tkwrapper import TkMenu, TkCommand, TkSeparator

class RunMenu(TkMenu):
    
    start_debugging: TkCommand()
    run_without_debugging: TkCommand()
    stop_debugging: TkCommand()
    restart_debugging: TkCommand()
    
    separator_1: TkSeparator()
    
    open_configurations: TkCommand()
    add_configuration: TkCommand()
    
    separator_2: TkSeparator()
    
    step_over: TkCommand()
    step_into: TkCommand()
    step_out: TkCommand()
    continue_: TkCommand()
    
    separator_3: TkSeparator()
    
    toggle_breakpoint: TkCommand()
    new_breakpoint: TkCommand()
    
    separator_4: TkSeparator()
    
    enable_all_breakpoints: TkCommand()
    disable_all_breakpoints: TkCommand()
    remove_all_breakpoints: TkCommand()
    
    separator_5: TkSeparator()
    
    install_additional_debuggers: TkCommand()
    
    
    
    
    