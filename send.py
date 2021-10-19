import smtplib
from email.mime.text import MIMEText


def send_mail(customer,dealer,rating):
    port=2525
    smtp_server='smtp.mailtrap.io'
    login='3fd42843b57691'
    password='96afd61c8906c2'
    message=f"<h3>New Feedback submission </h3><ul>,<li>customer:{customer}</li></ul?"
    sender_email='email1@example.com'
    reciever_email='email2@gexample.com'
    msg=MIMEText(message,'html')
    msg['Subject']='akdab feedback'
    msg['From']=sender_email
    msg['To']=reciever_email

    # send mail
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email,reciever_email,msg.as_string())
