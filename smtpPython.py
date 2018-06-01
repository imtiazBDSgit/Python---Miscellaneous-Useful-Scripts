import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
#Next, log in to the server
server.starttls()
server.login("test@gmail.com", "your passsword")
SUBJECT='Model Training Update :'
TEXT='Whats up dude? , Your model is still running , its epoch number 23 : still 7 more epochs to go.'
#Send the mail
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
server.sendmail("test@gmail.com", "test@gmail.com", message)