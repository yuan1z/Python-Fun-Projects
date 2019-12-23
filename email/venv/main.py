import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'xiaoshiyilangtxy@hotmail.com'
email['to'] = 'xiaoshiyilangtxy@gmail.com'
email['subject'] = 'You are the most genius guy in the world'
email.set_content('Using Python to send email to you')

with smtplib.SMTP(host='smtp.live.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('xiaoshiyilangtxy@hotmail.com', "grXrky8x")
    smtp.send_message(email)
    print('all good boss')