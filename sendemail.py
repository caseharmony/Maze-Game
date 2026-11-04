import os
import secrets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

def otp(recipient_email):
    # Generate a secure 6-digit OTP
    generated_otp = str(secrets.randbelow(900000) + 100000)
    
    # Load email and app password from environment variables
    sender_email = os.getenv("SENDER_EMAIL")
    acc_email = os.getenv("ACC_EMAIL")
    app_password = os.getenv("EMAIL_APP_KEY")
    
    if not sender_email or not app_password:
        raise ValueError("SENDER_EMAIL and EMAIL_APP_KEY must be set in environment variables.")

    # HTML Email Template
    subject = f"Your one-time verification key for your aMAZEing account is {generated_otp}"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>OTP Verification</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #121212; margin: 0; padding: 0;">
        <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #121212; padding: 40px 0;">
            <tr>
                <td align="center">
                    <table width="600" cellpadding="0" cellspacing="0" style="background: #1e1e1e; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.5); padding: 40px;">
                        <tr>
                            <td>
                                <!-- Logo / Image -->
                                <div style="text-align: center; margin-bottom: 25px;">
                                    <img src="https://i.postimg.cc/gXGrx3C2/image.png" alt="aMAZEing Logo" style="max-width: 150px; height: auto; display: block; margin: 0 auto;">
                                </div>

                                <h2 style="color: #ffffff; margin-top: 0; text-align: center;">aMAZEing Account Registration</h2>
                                
                                <p style="color: #dce4ee; font-size: 16px; line-height: 1.5;">Hello Dear User,</p>
                                <p style="color: #dce4ee; font-size: 16px; line-height: 1.5;">Enter the code given below to complete the registration process for your aMAZEing account.</p>
                                
                                <!-- OTP Box (Dark Theme with Orange Accent) -->
                                <div style="text-align: center; margin: 30px 0;">
                                    <span style="display: inline-block; background-color: #2b2b2b; color: #FF6505; font-size: 32px; font-weight: bold; letter-spacing: 6px; padding: 12px 24px; border-radius: 6px; border: 1px dashed #FF8C42;">
                                        {generated_otp}
                                    </span>
                                </div>
                                
                                <p style="color: #949a9f; font-size: 14px; line-height: 1.5; text-align: center;">If you didn't request this, you can safely ignore this email.</p>
                                
                                <hr style="border: none; border-top: 1px solid #333333; margin: 30px 0;">
                                <p style="color: #777777; font-size: 12px; text-align: center; margin-bottom: 0;">&copy; aMAZEing. All rights reserved.</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Setup MIME structure
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    
    # Attach HTML content
    msg.attach(MIMEText(html_content, "html"))

    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(acc_email, app_password)
        smtp.sendmail(acc_email, recipient_email, msg.as_string())
        smtp.quit()
    except:
        print(f"Error sending email")
        print(f"OTP: {generated_otp}")
    return generated_otp
otp("mazegameotp@gmail.com")