import csv
import tkinter as tk
from src.core.google.gmail import GmailBase

class MainpageController:
    def __init__(self,view) -> None:
        self.view = view
        


    def load_email_treeview(self,email_destination):
        self.email_lists = {}
        with open(email_destination, 'r') as csvfile:
            emails = csv.DictReader(csvfile)
            for id,email in enumerate(emails,start=1):
                to = email.get('Email')
                self.view.targetTreeview.insert('', tk.END,iid=id, values=(id,to))
                self.email_lists[id] = to
    
    def load_credentials(self,credentials_destination):
        self.gmail_client = GmailBase(credentials_destination)

    def sent_mail(self):
        for id,email in self.email_lists.items():
            subject = self.view.get_subject_input_column_value()
            body = self.view.get_body_input_column_value()

            self.gmail_client.create_message(to=email,subject=subject,body=body)
            print("Mail Sucessfuly sented to {} ,count {}".format(email,id))

        
