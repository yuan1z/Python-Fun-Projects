import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'xiaoshiyilangtxy@hotmail.com'
email['to'] = 'xiaoshiyilangtxy@gmail.com'
email['subject'] = 'You are the most genius guy in the world'
email.set_content(html.substitute(name = 'Zihao'),'html')

with smtplib.SMTP(host='smtp.live.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('xiaoshiyilangtxy@hotmail.com', "grXrky8x")
    smtp.send_message(email)
    print('all good boss')