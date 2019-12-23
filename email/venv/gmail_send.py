import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'xiaoshiyilangtxy@gmail.com'
email['to'] = 'xiaoshiyilangtxy@hotmail.com'
email['subject'] = 'You are the most genius guy in the world'
email.set_content('Using Python to send email to you')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('xiaoshiyilangtxy@gmail.com', 'SUlv19947.18')
    smtp.send_message(email)
    print('all good boss')