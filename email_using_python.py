import smtplib 
# creates SMTP session 
#To use Gmail, we have to select the port no 587 and
#turn ON the 'Access For Less Secure Apps' in the sender's gmail account.

s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls() 
# Authentication 
s.login("sender_email_id", "sender_email_pwd") 

message = "message to be sent"

s.sendmail("sender_email_id", "receiver_email_id", message) 

s.quit() 
