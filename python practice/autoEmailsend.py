import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('saklain108@gmail.com','email r password dibo lagibo')
server.sendmail('saklain108@gmail.com','saklain5153@gmail.com','sucess .. ho ho.. mail pothai asu mr email nkhula k....')