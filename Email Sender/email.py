import smtplib
t=input("Enter the email of recipient:")
content=input("Enter the content for sent:")
def sendEmail(t,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com","123456")
    server.sendmail("abc@gmail.com",t,content)
    server.close()
sendEmail(t,content)