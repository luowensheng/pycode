import tkinter
from tkinter import ttk
from typing import Any, Optional

class TkItem:
    def pack(self, master:tkinter.Tk):
        raise NotImplementedError()


def get_annotations(instance)->dict[str, Any]:
    return getattr(instance, "__annotations__", {}).items()

def get_label(key:str, name:Optional[str]):
    return ' '.join(key.split("_")).title() if name is None else name 

class TkApp(TkItem):
    def __init__(self, title:str="App", shape:tuple[int]=(600, 600)) -> None:
        self.tk = tkinter.Tk()
        self.tk.title(title)
        self.tk.geometry(f'{shape[0]}x{shape[1]}')
        
        for (key, value) in get_annotations(self):
            if isinstance(value, TkItem):
                value.pack(self.tk)
                
            
    def run(self):
        self.tk.mainloop()        


class TkCommand(TkItem):
    def __init__(self, name:Optional[str]=None, **kwargs) -> None:
        super().__init__()
        
        self.name = name
        self.kwargs = kwargs
        self.command = kwargs.get('command', lambda: None)
               
               
class TkSeparator(TkItem):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.kwargs = kwargs
        

# def tagHighlight(self):
#         start = "1.0"
#         end = "end"
         
#         for mylist in self.wordlist:
#             num = int(self.wordlist.index(mylist))
 
#             for word in mylist:
#                 self.T1.mark_set("matchStart", start)
#                 self.T1.mark_set("matchEnd", start)
#                 self.T1.mark_set("SearchLimit", end)
 
#                 mycount = IntVar()
                 
#                 while True:
#                     index= self.T1.search(word,"matchEnd","SearchLimit", count=mycount, regexp = False)
 
#                     if index == "": break
#                     if mycount.get() == 0: break
 
#                     self.T1.mark_set("matchStart", index)
#                     self.T1.mark_set("matchEnd", "%s+%sc" % (index, mycount.get()))
 
#                     preIndex = "%s-%sc" % (index, 1)
#                     postIndex = "%s+%sc" % (index, mycount.get())
                     
#                     if self.check(index, preIndex, postIndex):
#                         self.T1.tag_add(self.tags[num], "matchStart", "matchEnd")
                             
        
class TkMenu(TkItem):
    
    def __init__(self, name:Optional[str]=None, background_color:str="#1e1e1e", **kwargs) -> None:
        self.background_color = background_color
        kwargs["tearoff"] = kwargs.get("tearoff", 0)
        self.kwargs = kwargs
        self.name = name
          
    
    def pack(self, master: tkinter.Tk):
        
        self.menu_bar = tkinter.Menu(master, background=self.background_color, **self.kwargs)

        for (key, value) in get_annotations(self):
            if isinstance(value, TkMenu):
               label = get_label(key, value.name)
               value.pack(master)
               
               self.menu_bar.add_cascade(label=label, menu=value.menu_bar) #, **value.kwargs)
            
            elif isinstance(value, TkCommand):
                label = get_label(key, value.name)
                self.menu_bar.add_command(label=label, command=value.command, **value.kwargs)
            
            elif isinstance(value, TkSeparator):
                self.menu_bar.add_separator(**value.kwargs)    
                   
        
        master.config(menu=self.menu_bar)           

class TkText(TkItem):
    def __init__(self, background_color="white") -> None:
        super().__init__()
        self.background_color = background_color
        self.content = ""
        
    def pack(self, master: tkinter.Tk):
        text = tkinter.Text(
            master, # background=self.background_color,
            #cursor="xterm white", foreground="black"
        )
       # text.configure(font=("Arial", 19, "normal"))
        # text.insert("1.0", "red")
        # text.content = text.get("1.0", tkinter.END)
        def add_text(s: tkinter.Event):
            content = text.get("1.0", tkinter.END) + s.char
            print(f'{content=}')
            lines = content.split("\n")
            last_line = lines[-1]
            last_line_words = last_line.split()
            if not last_line_words: return
            
            print(f'{last_line_words=}')
            last_word = last_line_words[-1]
            if last_word == "red":
                match_start = f"{1+len(lines)}.{len(last_line)-3}"
                print(f'{match_start=}')
                text.mark_set("matchStart", match_start)
                text.mark_set("matchEnd", tkinter.END)
                text.tag_add("red", "matchStart", "matchEnd")
                
            print("[",last_word, "]", (s.delta, s.height, s.width, s.num, s.x))
            # print(f"Got {s.char} {s.type}  {s.keycode} {s.keysym_num}")
            # text.add(s)
        text.bind("<Key>", add_text)
        text.bind('<Control-Key-C>', add_text)
        text.tag_configure("red", foreground="red")
        # text.mark_set("matchStart", "1.0")
        # text.mark_set("matchEnd", tkinter.END)
        # text.tag_add("red", "matchStart", "matchEnd")
        # text.hu("word", "red")
        text.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

class TkFrame(TkItem):
    def __init__(self, background_color:str="#1e1e1e") -> None:
        self.background_color = background_color

    def pack(self, master: tkinter.Tk):
        
        self.item = tkinter.Frame(master, bg=self.background_color, width=600, height=600)
        for (key, value) in get_annotations(self):

            if isinstance(value, TkText):
               value.pack(self.item)

            elif isinstance(value, TkNotebook):
                value.pack(master)
                
        self.item.pack(fill=tkinter.BOTH, expand=1)
                
class TkNotebook(TkItem):

    def pack(self, master: tkinter.Tk):
        
        notebook = ttk.Notebook(master)
        for (key, value) in get_annotations(self):

            if isinstance(value, TkFrame):
                value.pack(notebook)
                notebook.add(value.item, text="Untitled"+f'({key})')

        notebook.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)
        
        