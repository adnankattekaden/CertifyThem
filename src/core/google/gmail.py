from src.core.google.google_authentication import Create_Service
import base64
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import mimetypes
from email import encoders

class GmailBase:
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']
    
    def __init__(self) -> None:
        """
        Create an instance of Gmail
        """




    def authenticate(self, client_file):
        self.service = Create_Service(client_file,self.API_NAME,self.API_VERSION,self.SCOPES)
        self.service.users().getProfile(userId='me').execute()
        return True


        
        
    def create_message(self,to,subject,body,message_type='plain',user_id='me'):
        """
        Send an email message.
        
        Args:
            to: Email address of the receiver
            subject: The subject of the email message
            body: The Body (content) of email
            message_type: HTML / Plain Text 
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
        
        Returns:
            Message.
        """
        
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = to
        mimeMessage['subject'] = subject
        mimeMessage.attach(MIMEText(body,message_type))

        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = self.service.users().messages().send(userId=user_id,body={'raw':raw_string}).execute()
        return message


    def create_message_with_attachments(self,to,subject,body,file_attachments,message_type):
        """Create a message With attachments.
        Args:
            to: Email address of the receiver.
            subject: The subject of the email message.
            body: The text of the email message.
            file_attachments: The paths to the file to be attached. ['path1.jpg','path2.pdf'] -> DataType
        Returns:
            Sent Message With Files Attached.
        """
        
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = to
        mimeMessage['subject'] = subject
        mimeMessage.attach(MIMEText(body,message_type))

        for attachment in file_attachments:

            content_type,encoding = mimetypes.guess_type(attachment)
            main_type,sub_type = content_type.split('/',1)
            file_name = os.path.basename(attachment)
            

            f = open(attachment,'rb')

            myfile = MIMEBase(main_type,sub_type)
            myfile.set_payload(f.read())
            myfile.add_header('Content-Disposition', 'attachment', filename=file_name)
            encoders.encode_base64(myfile)
            f.close()
            mimeMessage.attach(myfile)

        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        msg = self.service.users().messages().send(userId='me',body={'raw':raw_string}).execute()
        return msg