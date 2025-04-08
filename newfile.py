import base64
import os
from email.message import EmailMessage
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
print("Current working directory",os.getcwd())
print("Files here",os.listdir())

# Login to Gmail using OAuth
def gmail_login():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('gmail', 'v1', credentials=creds)

# Create and send an email
def send_email(service):
    msg = EmailMessage()
    msg.set_content("Hello Ayush! This is a test email sent using the Gmail API.")
    msg['To'] = 'receiver@example.com'         # Change to target email
    msg['From'] = 'your_email@gmail.com'       # Change to your Gmail
    msg['Subject'] = 'Test Email from Python'

    # Encode the message
    encoded_msg = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    send_body = {'raw': encoded_msg}

    # Send the message
    result = service.users().messages().send(userId='me', body=send_body).execute()
    print(f'Message sent! ID: {result['id']}')  # Make sure quotes are correct here

# Main function to run everything
if __name__ == '__main__':
    service = gmail_login()
    send_email(service)