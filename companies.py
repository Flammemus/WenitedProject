class Company:
    companyList = []
    def __init__(self, name, status, numberOfMeetings, emails):
        self.name = name
        self.status = status
        self.numberOfMeetings = numberOfMeetings
        self.emails = emails
        Company.companyList.append(self)

wenited = Company(
    name="Wenited",
    status="Progressing",
    numberOfMeetings="11",
    emails=["Hey! You need to be in a meeting at 10am.", "Remember to make the GoFile feature that we talked about. the one where you need to summarize all emails from a spesific company"]
)

amazon = Company(
    name="Amazon",
    status="Slow",
    numberOfMeetings="3",
    emails=["Hey! You need to be in a meeting at 5pm, you have to be there. very important", "please restructure our database for more user friendly use"]
)

google = Company(
    name="Google",
    status="Active",
    numberOfMeetings="8",
    emails=["Reminder: Quarterly review meeting tomorrow.", "Proposal for new AI-driven project."]
)

microsoft = Company(
    name="Microsoft",
    status="Stalled",
    numberOfMeetings="5",
    emails=["Update on software licensing agreement.", "Request for collaboration on cloud computing project."]
)

apple = Company(
    name="Apple",
    status="On hold",
    numberOfMeetings="2",
    emails=["Invitation to Apple's annual developer conference.", "Discussion on potential partnership opportunities."]
)

facebook = Company(
    name="Facebook",
    status="Exploratory",
    numberOfMeetings="4",
    emails=["Presentation on ad targeting algorithms.", "Interest in joint research on social media trends."]
)

tesla = Company(
    name="Tesla",
    status="Active",
    numberOfMeetings="6",
    emails=["Tesla Model Y delivery update.", "Discussion on renewable energy initiatives."]
)
