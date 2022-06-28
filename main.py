from src.google.gmail import GmailBase


CLIENT_FILE = "credentials.json"
client = GmailBase(CLIENT_FILE)

to = 'adnankattekaden2020@gmail.com'
subject = 'Congratulations!! You had successfully completed the bootcamp Build.myweb v2'
body = """
<p>Simple HTML.</p>
<h3><em>So very simple.</em></h3>
<p><span style="color: #ff0000;">Lame joke that follows.</span></p>
<p>
  <span style="color: #ff0000;"
    ><img
      src="https://i.imgur.com/mxVlFHM.jpeg"
      alt="Lame joke"
      width="245"
      height="221"
  /></span>
</p>
<h2 style="padding-left: 30px;">do you?</h2>
<ul>
  <li>yes</li>
  <li>no</li>
  <li><strong>not entirely sure</strong></li>
</ul>
"""

client.create_message(to,subject,body)
