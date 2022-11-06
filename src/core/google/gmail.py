from src.core.google.google_authentication import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
