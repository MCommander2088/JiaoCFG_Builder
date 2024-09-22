import random
import sys
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askdirectory,asksaveasfile
from tkinter.messagebox import showerror,showinfo,showwarning

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_m1cuth8k = self.__tk_button_m1cuth8k(self)
        #self.tk_button_m1cuuyzn = self.__tk_button_m1cuuyzn(self)
        self.tk_text_m1cv1o7c = self.__tk_text_m1cv1o7c(self)
    def __win(self):
        self.title("JiaoCFG一键生成")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def command1(self):
        text = self.tk_text_m1cv1o7c.get(1.0,END)
        print(text)
        if not text.replace('\n','') == '':
            generator.generate(text)
    
    def __tk_button_m1cuth8k(self,parent):
        btn = Button(parent, text="生成", takefocus=False,command=self.command1)
        btn.place(x=320, y=42, width=82, height=38)
        return btn
    '''def __tk_button_m1cuuyzn(self,parent):
        btn = Button(parent, text="保存", takefocus=False,)
        btn.place(x=317, y=100, width=82, height=38)
        return btn'''
    def __tk_text_m1cv1o7c(self,parent):
        text = Text(parent)
        text.place(x=14, y=18, width=218, height=461)
        return text
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_m1cuth8k.bind('<click>',self.ctl.operate)
        pass
    def __style_config(self):
        pass

class String_Operation:
    def __init__(self,key_talk,key_reset,key_last) -> None:
        if (not key_talk) or (not key_last) or (not key_reset):
            raise ValueError
        self.k_t = key_talk
        self.k_l = key_last
        self.k_r = key_reset
    
    def generate(self,usr_input):
        self.strings = usr_input.split('\n')
        print(self.strings)
        self.result = ''
        for s in range(len(self.strings)):
            if s == 0:
                self.result = f"""{self.result}\nalias command{s} "say {self.strings[s]};bind {self.k_t} command{s+1}" """
                continue
            elif s == len(self.strings)-1:
                self.result = f"""{self.result}\nalias command{s} "say {self.strings[0]};bind {self.k_t} command0;bind {self.k_l} command{s-1};command0" """
                continue
            self.result = f"""{self.result}\nalias command{s} "say {self.strings[s]};bind {self.k_t} command{s+1};bind {self.k_l} command{s-1}" """
        self.result = f"{self.result}\nbind {self.k_t} command0"

        path_ = str(asksaveasfile(title="选择保存路径",filetypes=[('CFG文件','.cfg')],initialdir='.').name).replace("\\","/")

        with open(f"{path_}","w+",encoding='utf-8') as f:
            f.write(self.result)
            f.close()

        

        return self.result

def main():
    global generator
    generator = String_Operation('f','0','v')
    '''
    output_path = "D:\SteamLibrary\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg".replace("\\","/")

    with open(f"{output_path}/output.cfg","w+") as f:
        f.write(generator.generate("""1
                       2
                       3"""))
        f.close()
    '''

    win = WinGUI()
    win.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        showerror(title="程序出现错误！",message=e)
        sys.exit(e)
