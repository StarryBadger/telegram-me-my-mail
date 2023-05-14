#!/usr/bin/python3
import imaplib
import email
from email.header import decode_header
from datetime import datetime

username = "throwaway2441139@outlook.com"
password = "telegrammemymail@github"
imap_server = "outlook.office365.com"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)
status, messages = imap.select("INBOX")
N = 3
messages = int(messages[0])

for i in range(messages, 0, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding)
            date, encoding = decode_header(msg["Date"])[0]
            if isinstance(date, bytes):
                date = date.decode(encoding)
            if i==messages:
                newestdate=date
            date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z")
            with open('prevtime.txt', 'r') as file:
                prevDate = file.read()
            prevDate = datetime.strptime(prevDate, "%a, %d %b %Y %H:%M:%S %z")
            if prevDate>=date:
                break
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            print("Subject:", subject)
            print("Time: ",date)
            print("From:", From)
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        print(body)
                    elif "attachment" in content_disposition:
                        body="Image attachment detected"
                        print(body)
                        filepath="./img.png"
                        open(filepath, "wb").write(part.get_payload(decode=True))
            else:
                content_type = msg.get_content_type()
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    print(body)
with open('prevtime.txt', 'w') as file:
    file.write(newestdate)
imap.close()
imap.logout()
