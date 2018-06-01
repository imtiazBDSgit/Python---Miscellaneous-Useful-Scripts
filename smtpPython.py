import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
#Next, log in to the server
server.starttls()
server.login("test@gmail.com", "your passsword")
SUBJECT='Model Training Update :'
TEXT='Whats up dude?'
#Send the mail
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
server.sendmail("test@gmail.com", "test@gmail.com", message)
