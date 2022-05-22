import smtplib
from email.message import EmailMessage

def send(str, to):
  user = EMAIL_ADDRESS
  password = PASSWORD

  carriers = ["@txt.att.net", "@messaging.sprintpcs.com", "@tmomail.net", 
              "@vtext.com", "@myboostmobile.com", "@sms.mycricket.com"]
  
  for carrier in carriers:
    ext_to = to + carrier
    print(ext_to)

    msg = EmailMessage()
    msg.set_content(str)
    msg['to'] = ext_to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
