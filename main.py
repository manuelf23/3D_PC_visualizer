from tkinter import Tk, Frame
from views.home import Home

class MainApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.camsInfo = {}
        self.protocol("WM_DELETE_WINDOW", self.close)

        self.title('Visualizador nube de puntos')
        width = 500
        height = 130
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.resizable(0, 0)

        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.pages = (Home,)

        for F in self.pages:
            frame = F(self, container)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame('Home')
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def close(self, *args):
        self.destroy()

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
