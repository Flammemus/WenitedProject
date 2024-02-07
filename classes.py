class Company:
    companyList = []
    def __init__(self, name, status, timesMetWith, emails):
        self.name = name
        self.status = status
        self.timesMetWith = timesMetWith
        self.emails = emails
        Company.companyList.append(self)

wenited = Company(
    name="Wenited",
    status="Good",
    timesMetWith="11",
    emails=["Hey! You need to be in a meeting at 10am.", "Remember to make the GoFile feature that we talked about. the one where you need to summarize all emails from a spesific company"]
)

amazon = Company(
    name="Amazon",
    status="Mediocre",
    timesMetWith="3",
    emails=["Hey! You need to be in a meeting at 5pm, you have to be there. very important", "please restructure our database for more user friendly use"]
)