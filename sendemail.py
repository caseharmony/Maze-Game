import smtplib
import secrets
import os
def otp(recipient_email,appkey=os.getenv('EMAIL')):
    otp = str(secrets.randbelow(900000)+100000)
    try:
        smtp=smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('mazegameotp@gmail.com',appkey)
        msg ="""From: mazegameotp@gmail.com
        Subject: OTP for Mazegame Login

        your OTP to Login to Mazegame is:
        """
        msg=msg+otp
        smtp.sendmail("mazegameotp@gmail.com", recipient_email, msg)
        smtp.quit()
    except:
        print(otp)
    return otp
