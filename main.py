from src.google.gmail import GmailBase
import csv
import tkinter as tk
from view.main_page_view import MainPage



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
        pages = (MainPage,)

        for page in pages:
            frame = page(master=main_frame)
            self.frames[page] = frame
            frame.place(relx=0,rely=0) 
        
        self.show_frame(MainPage)


    def show_frame(self,frame_name):
        print(self.frames)
        frame = self.frames[frame_name]
        frame.tkraise()


        



if __name__ == "__main__":
    root = Application()
    root.mainloop()

# CLIENT_FILE = "credentials.json"
# client = GmailBase(CLIENT_FILE)

# with open('Build.MyWebMeetUpEmailList.csv', 'r') as csvfile:
#     emails = csv.DictReader(csvfile)
#     for counts,email in enumerate(emails):
#         to = email.get('Email')

#         subject = ''
        # body = """"""
#         client.create_message(to,subject,body,message_type='html')
#         print("Mail Sucessfuly sented to {} ,count {}".format(to,counts))
