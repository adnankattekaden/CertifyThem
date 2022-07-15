
from itertools import count
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import filedialog
import os

from src.controller.main_page_controller import MainpageController

class MainPageView(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.controller = MainpageController(view=self)
        self._setup_ui()

        


    def _setup_ui(self):
        header_label = tk.Label(self.master,text='CertifyThem',font=('Verdana Pro Cond Black',25))
        header_label.place(rely=0.04,relx=0.50,anchor='center')
        author_label = tk.Label(self.master,text="By Adnan Kattekaden")
        author_label.place(rely=0.07,relx=0.60)

        credentialsLabel = tk.Label(self.master,text='Load Credentials')
        credentialsLabel.place(rely=0.12, relx=0.02)
        self.loadCredentialsDestinationLabel = tk.Label(self.master,relief="ridge",anchor="w")
        self.loadCredentialsDestinationLabel.place(rely=0.15,relx=0.02, height=23,width=375)
        loadcredentialsBtn = ttk.Button(self.master,text='Browse ...',command=self._set_credentials_destination)
        loadcredentialsBtn.place(rely=0.15,relx=0.40)

        loadEmailLabel = tk.Label(self.master, text="Load Emails")
        loadEmailLabel.place(rely=0.22,relx=0.02)
        self.loadEmailDestinationLabel = tk.Label(self.master,relief='ridge',anchor='w')
        self.loadEmailDestinationLabel.place(rely=0.25,relx=0.02,height=23,width=375)
        loadEmailBtn = ttk.Button(self.master,text="Browse ...",command=self._set_email_destination)
        loadEmailBtn.place(rely=0.25,relx=0.40)


        targetLabelFrame = tk.LabelFrame(self.master,text='Targets')
        targetLabelFrame.place(rely=0.32,relx=0.02,height=300,width=470)
        self.targetTreeview = ttk.Treeview(targetLabelFrame,show="headings")
        self.targetTreeview.place(relheight=1,relwidth=1)
        self.targetTreeview["columns"] = ['ID',"Emails"]

        for column_name in self.targetTreeview["columns"]:
            self.targetTreeview.heading(column_name,text=column_name)


        sentMailBtn = ttk.Button(self.master,text="Sent Emails",command=self.controller.sent_mail)
        sentMailBtn.place(rely=0.84,relx=0.40)

        subjectLabelFrame = tk.LabelFrame(self.master,text='Subject')
        subjectLabelFrame.place(rely=0.12,relx=0.50,height=40,width=500)
        self.subjectInputColumn = tk.Entry(subjectLabelFrame)
        self.subjectInputColumn.place(relheight=1,relwidth=1)

        bodyLabelFrame = tk.LabelFrame(self.master,text='Body')
        bodyLabelFrame.place(rely=0.20,relx=0.50,height=475,width=500)
        self.bodyInputColumn = tk.Text(bodyLabelFrame)
        self.bodyInputColumn.place(relheight=1,relwidth=1)
        bodyInputColumnScrollY = tk.Scrollbar(bodyLabelFrame,orient='vertical',command=self.bodyInputColumn.yview)
        self.bodyInputColumn.config(yscrollcommand=bodyInputColumnScrollY.set)
        bodyInputColumnScrollY.pack(side='right',fill='y')

    def _windows_dialogbox(self,file_type,file_extention):
        WORKING_DIR = os.getcwd()
        
        filetypes = (
            (file_type, '*.{}'.format(file_extention)),
        )

        selection = filedialog.askopenfilename(title='Choose Credentials',initialdir=WORKING_DIR,filetypes=filetypes)
        return selection

    def _set_credentials_destination(self):
        credential_destination = self._windows_dialogbox('JSON','json')
        self.loadCredentialsDestinationLabel['text'] = credential_destination
        self.controller.load_credentials(credential_destination)

    def get_credentials_destination(self):
        return self.loadCredentialsDestinationLabel['text']
    
    def _set_email_destination(self):
        email_destination = self._windows_dialogbox('CSV','csv')
        self.loadEmailDestinationLabel['text'] = email_destination
        
        self.controller.load_email_treeview(email_destination=email_destination)               
        return email_destination

    def get_subject_input_column_value(self):
        return self.subjectInputColumn.get()
    
    def get_body_input_column_value(self):
        return self.bodyInputColumn.get("1.0",'end')


