import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(sender, passwd, receiver, subject, html):
    ''' It sends the email to client as per dynamic argumets 
	sender :  email id from which we need to send mail
	passwd : password of sendor email
	receiver : Lis of Email ids on which we eed to send email
	subject : mail subject to send
	html : Mail body string, uses html formatting
	'''
    msg = MIMEMultipart("alternative")
    COMMASPACE = ', '
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = COMMASPACE.join(receiver)
    print("Receiver is ", receiver)
    part2 = MIMEText(html, "html")
    msg.attach(part2)
    try:
        # con = smtplib.SMTP("smtp.office365.com", 587)
        con = smtplib.SMTP("smtp.ionos.com", 587)
        con.ehlo()
        con.starttls()
        con.ehlo()
        con.login(sender, passwd)
        ack = con.sendmail(sender, receiver, msg.as_string())
        con.ehlo()
    except Exception as er:
        print("Error while sending mail : ",er)
        return er
    con.quit()
    return ack

