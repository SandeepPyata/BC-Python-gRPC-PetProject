import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def Send_Email(customer_email, content, optional=""):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "pyatasandeepsandy@gmail.com"
    receiver_email = customer_email

    # App-specific password for Linux
    password = 'hgylnrslrexnzztw'

    message = MIMEMultipart("alternative")
    message["Subject"] = "Bike Booking"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """\
        Hi!
    """

    html = f"""\
    <html>
    <body>
        <b>{content}</b>
        <p>{optional}</p>
    </body>
    </html>
    """

    part1 = MIMEMultipart(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
