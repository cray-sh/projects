"""
Author: Coursera
Date: Unknown, Date Retrieved: 2023.02.02

This is the email module that the project wants me to use instead of
creating my own. I've copied it here to see how it works etc
"""


#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
    """Creates an Email with an attachment."""
    #basic email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    
    #process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)
    return message

def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()