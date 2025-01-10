import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Bob' # Name
email['to'] = 'john@gmail.com' # Email address
email['subject'] = 'Check up'

email.set_content(html.substitute(name = 'Bob'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: # For gmail, but you can change it
	smtp.ehlo()
	smtp.starttls()
	smtp.login('bob@gmail.com', 'hshsjjsjsjs') # Sender's email address and hashed password (which you can obtain from your email settings)
	smtp.send_message(email)
	print('all good')
