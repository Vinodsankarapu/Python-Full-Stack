'''
python --> automation-->email automation
simple mail automation
mail otp
mail with subject and attachments
cbds raaa demy fmyb 

#simple mail automation
#smtp--> simple mail transfer protocol
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
server.starttls()
server.login("vinodsankarapu4@gmail.com", "llum ypos mdfo jwtl")
msg="rohit haa na frienduuu "
server.sendmail("vinodsankarapu4@gmail.com","raavi.rohit08@gmail.com",msg)
server.quit()
print("mail sent")
import math
import random
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("vinodsankarapu4@gmail.com","llum ypos mdfo jwtl")
msg =random.randint (1969,2069)
server.sendmail("vinodsankarapu4@gmail.com",
                "raavi.rohit08@gmail.com",str(msg))
#close the connection
server.quit()
print("mail sent")'''

import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
From="vinodsankarapu4@gmail.com"
to="raavi.rohit08@gmail.com@gmail.com"
subject="python full stack training "
msg=MIMEMultipart()
#print(msg)
#pritn(type(msg))
msg['from']=From
msg['to']=to
msg['subject']=subject
text="rohit na frienduuu"
msg.attach(text)
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server)
server.starttls()
server.login("vinodsankarapu4@gmail.com","llum ypos mdfo jwtl ")
server.sendmail(From,to,text)
server.quit()
print("mail sent")
