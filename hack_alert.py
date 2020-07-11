import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
   
fromaddr = "siddcool1011@gmail.com"
toaddr = "coolsidd1997@gmail.com"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = "siddcool1011@gmail.com" 
  
# storing the receivers email address  
msg['To'] = "coolsidd1997@gmail.com" 
  
# storing the subject  
msg['Subject'] = "!Warning...DDOS Attack!"
  
# string to store the body of the mail 
body = "HEY!!!!!SOmeone used DDOS attack on your server...we have temporarily blocked that IP which seems suspicious. ...come and watch for your satisfaction........"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "/root/all_ip_list.txt"
attachment = open("/root/all_ip_list.txt", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "Jaishreeram@1011") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 
