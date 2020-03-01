import smtplib
email=################
password=#############
mailto=##################
msg='Test Email using SMTP'
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(email, password)
mailServer.sendmail(email, mailto , msg)
print(" \n Sent!")
mailServer.quit()