import csv
import tkinter as tk
from requests import head
from src.core.google.gmail import GmailBase
import os


class MainpageController:
    def __init__(self,view) -> None:
        self.view = view
        self.gmail_client = GmailBase()
        
    def load_email_treeview(self,email_destination):
        self.email_lists = {}
        with open(email_destination, 'r',encoding='utf-8-sig') as csvfile:
            emails = csv.DictReader(csvfile)
            
            for id,email in enumerate(emails,start=1):
                to = email.get('email')
                name = email.get('name')

                self.view.targetTreeview.insert('', tk.END,iid=id, values=(id,name,to))
                self.email_lists[id] = {'email':to,'name':name}


                
    
    def load_credentials(self,credentials_destination):
        self.gmail_client.authenticate(credentials_destination)

    def get_file_path(self,filename,path="/mulearn/FossHack Certificates/"):
        filterd = []

        working_dir = os.path.join(os.getcwd()) + path + filename+'.pdf'
        filterd.append(working_dir)

            
            # for root,dir,files in os.walk(working_dir):
            #     if filename in files:
            #         filterd.append(os.path.join(root,filename))

        return filterd
        
    def sent_mail(self):

        for id,email in self.email_lists.items():
            name = email.get('name')
            email = email.get('email')
            subject = self.view.get_subject_input_column_value()
            body = self.view.get_body_input_column_value()
            body = body.format(name=name)

            # file_attachments_list = self.get_file_path(filename=name)
            self.gmail_client.create_message(to=email,subject=subject,body=body,message_type='html')
            # self.gmail_client.create_message_with_attachments(to=email,subject=subject,body=body,file_attachments=file_attachments_list,message_type='html')
            print("Mail Sucessfuly sented to {} ,count {}".format(email,id))

        
