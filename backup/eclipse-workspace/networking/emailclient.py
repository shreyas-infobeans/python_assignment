import smtplib
from email.mime.text import MIMEText

body = "This is the test email from python tutorial"

msg = MIMEText(body)
msg['From'] = "shreyas.dhokte@infobeans.com"
msg['To'] = "shreyas.dhokte@infobeans.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("shreyas.dhokte@infobeans.com",'krvt tndn oinz aiso')    

server.send_message(msg)

print("mail sent")

server.quit()