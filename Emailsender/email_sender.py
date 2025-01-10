import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Babacan Guven'
email['to'] = 'babagvn1903@gmail.com'
email['subject'] = 'You won £1,000,000'

email.set_content(html.substitute(name = 'Bob'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('babaqpr@gmail.com', 'tqwglncozlqkvmdh')
	smtp.send_message(email)
	print('all good')