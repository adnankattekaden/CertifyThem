import tkinter as tk
from src.view.main_page_view import MainPageView



HEIGHT = 600
WIDTH = 1024

class Application(tk.Tk):
    TITLE = "CertifyThem"
    def __init__(self):
        super().__init__()
        self.title(self.TITLE)
        self.geometry(f"{WIDTH}x{HEIGHT}")

        main_frame = tk.Frame(self,height=HEIGHT,width=WIDTH)
        main_frame.pack_propagate(0)
        main_frame.pack(fill='both',expand=True)

        self.frames = {}
        pages = (MainPageView,)

        for page in pages:
            frame = page(master=main_frame)
            self.frames[page] = frame
            frame.place(relx=0,rely=0) 
        
        self.show_frame(MainPageView)


    def show_frame(self,frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


        



if __name__ == "__main__":
    root = Application()
    root.resizable(height = 0, width = 0)
    root.mainloop()
