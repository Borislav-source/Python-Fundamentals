class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


class MailBox:
    def __init__(self):
        self.emails = []

    def add_email(self, email: Email):
        self.emails.append(email)

    def send_emails(self, sent_mails):
        for index in sent_mails:
            self.emails[index].send()

    def print_mailbox(self):
        for email in self.emails:
            print(email.get_info())


mailbox = MailBox()
while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = list(command.split())
    email = Email(sender, receiver, content)
    mailbox.add_email(email)

sent_mails = list(map(int, input().split(", ")))
mailbox.send_emails(sent_mails)
mailbox.print_mailbox()
