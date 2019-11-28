from email.mime.text import MIMEText
import smtplib

# MIMEText, first phrase is the mail contents,.
# 2nd phrase is the type of the email. 'plain' is txt only.
msg = MIMEText('Hello, sent by Python...', 'plain', 'utf-8')

# input sender's email address and password:
from_addr = input('From: ')
password = input('Password: ')

# input receiver's email address
to_addr = input('To: ')

# input SMTP server address
smtp_server = input(' SMTP server: ')

server = smtplib.SMTP_SSL(smtp_server, 465) # default socket number 25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()