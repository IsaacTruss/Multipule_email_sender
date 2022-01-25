import smtplib
from socket import gaierror

port = 2525
smtp_server = "smtp.mailtrap.io"
login = "Your login" # your login generated by Mailtrap
password = "Your Password" # your password generated by Mailtrap

# specify the sender’s and receiver’s email addresses
sender = "from@example.com"
receiver = "to@example.com"

# message 
message = """Subject: Test
To: {recipient}
From: {sender}

Hi {name}, This is a test"""

sender = "sender@example.com"

# searches through contacts.csv to find the name and email address of a person and sends them an email
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login(login, password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)  # it skips the header row
        for name, email in reader:
            server.sendmail(
               sender,
                email,
                message.format(name=name, recipient=email, sender=sender)
            )
            print(f'Sent to {name}')
