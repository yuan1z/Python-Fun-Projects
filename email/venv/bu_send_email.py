import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'yuan1z@bu.edu'
email['to'] = 'xiaoshiyilangtxy@hotmail.com'
email['subject'] = 'You are the most genius guy in the world'
email.set_content('Using Python to send email to you')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yuan1z@bu.edu', 'SUlv19947.18')
    smtp.send_message(email)
    print('all good boss')