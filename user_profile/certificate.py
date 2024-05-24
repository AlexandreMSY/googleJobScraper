from datetime import date

class Certificate:
    def __init__(self, certificateName : str, issueDate: date):
        self.name = certificateName,
        self.issueDate = issueDate