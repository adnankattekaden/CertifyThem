from doctest import master
import tkinter as tk
from tkinter import ttk,messagebox

class MainPage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        
        header_label = tk.Label(master,text='CertifyThem',font=('Verdana Pro Cond Black',25))
        header_label.place(rely=0.04,relx=0.50,anchor='center')
        author_label = tk.Label(master,text="By Adnan Kattekaden")
        author_label.place(rely=0.07,relx=0.60)


        credentialsLabel = tk.Label(master,text='Load Credentials')
        credentialsLabel.place(rely=0.12, relx=0.02)
        self.loadCredentialsDestinationLabel = tk.Label(master,relief="ridge",anchor="w")
        self.loadCredentialsDestinationLabel.place(rely=0.15,relx=0.02, height=23,width=375)
        loadcredentialsBtn = ttk.Button(master,text='Browse ...')
        loadcredentialsBtn.place(rely=0.15,relx=0.40)


        loadEmailLabel = tk.Label(master, text="Load Emails")
        loadEmailLabel.place(rely=0.22,relx=0.02)
        self.loadEmailDestinationLabel = tk.Label(master,relief='ridge',anchor='w')
        self.loadEmailDestinationLabel.place(rely=0.25,relx=0.02,height=23,width=375)
        loadEmailBtn = ttk.Button(master,text="Browse ...")
        loadEmailBtn.place(rely=0.25,relx=0.40)


        targetLabelFrame = tk.LabelFrame(master,text='Targets')
        targetLabelFrame.place(rely=0.32,relx=0.02,height=300,width=470)

        self.targetTreeview = ttk.Treeview(targetLabelFrame)
        self.targetTreeview.place(relheight=1,relwidth=1)

        self.targetTreeview["columns"] = ["email"]
        self.targetTreeview["show"] = "headings"

        for column_name in self.targetTreeview["columns"]:
            self.targetTreeview.heading(column_name,text=column_name)


        sentMailBtn = ttk.Button(master,text="Sent Emails")
        sentMailBtn.place(rely=0.84,relx=0.40)


        resultOutputLabelFrame = tk.LabelFrame(master,text='Result')
        resultOutputLabelFrame.place(rely=0.15,relx=0.50,height=475,width=500)

        self.resultOutputTextbox = tk.Text(resultOutputLabelFrame)
        self.resultOutputTextbox.place(relheight=1,relwidth=1)
        resultOutputTextboxScrollY = tk.Scrollbar(resultOutputLabelFrame,orient='vertical',command=self.resultOutputTextbox.yview)
        self.resultOutputTextbox.config(yscrollcommand=resultOutputTextboxScrollY.set)
        resultOutputTextboxScrollY.pack(side='right',fill='y')



        


