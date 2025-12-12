import smtplib
import random
def otp(recipient_email,appkey='utov sfiw dmdy qwco'):
    smtp=smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('mazegameotp@gmail.com',appkey)
    otp = str(random.randint(100000, 999999))
    msg ="""From: mazegameotp@gmail.com
    Subject: OTP for Mazegame Login

    your OTP to Login to Mazegame is:
    """
    msg=msg+otp
    smtp.sendmail("mazegameotp@gmail.com", recipient_email, msg)
    smtp.quit()
    print(otp)
    return otp
