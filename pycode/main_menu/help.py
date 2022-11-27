from tkwrapper import TkMenu, TkCommand, TkSeparator

class HelpMenu(TkMenu):
    
    get_status: TkCommand()
    show_all_commands: TkCommand()
    documentation: TkCommand()
    editor_playground: TkCommand()
    show_release_notes: TkCommand()
    
    separator_1: TkSeparator()
    
    keyboard_shortcut_reference: TkCommand()
    video_tutorials: TkCommand()
    tips_and_tricks: TkCommand()
    
    separator_2: TkSeparator()
    
    join_us_on_twitter: TkCommand()
    search_feature_requests: TkCommand()
    report_issue: TkCommand()
    
    separator_3: TkSeparator()
    
    view_license: TkCommand()
    privacy_statement: TkCommand()
    
    separator_4: TkSeparator()
    
    toggle_developper_tools: TkCommand()
    open_process_explorer: TkCommand()
    
    separator_5: TkSeparator()
    
    check_for_updates: TkCommand()
    
    separator_6: TkSeparator()

    about: TkCommand()
    
    
    
    