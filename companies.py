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
    emails=[
        "Hey! You need to be in a meeting at 10am.",
        "Remember to make the GoFile feature that we talked about. The one where you need to summarize all emails from a specific company.",
        "Final reminder for the quarterly performance review tomorrow. Please be prepared with your updates.",
        "Follow-up on the discussion about expanding into international markets. Can you provide more details?",
        "Action item: Review the latest user feedback and come up with a plan for improvements.",
    ]
)

amazon = Company(
    name="Amazon",
    status="Slow",
    numberOfMeetings="3",
    emails=[
        "Hey! You need to be in a meeting at 5pm, you have to be there. Very important.",
        "Please restructure our database for more user-friendly use.",
        "Update on the latest sales figures. We're seeing a slight decrease in revenue.",
        "Discussion on potential collaborations with third-party sellers. What are your thoughts?",
        "Reminder: Deadline for submitting project proposals is approaching. Make sure to finalize yours.",
    ]
)

google = Company(
    name="Google",
    status="Active",
    numberOfMeetings="8",
    emails=[
        "Reminder: Quarterly review meeting tomorrow.",
        "Proposal for new AI-driven project.",
        "Update on the latest developments in machine learning algorithms.",
        "Request for feedback on the beta version of our new software.",
        "Invitation to a webinar on cloud computing trends. Don't miss out!",
    ]
)

microsoft = Company(
    name="Microsoft",
    status="Stalled",
    numberOfMeetings="5",
    emails=[
        "Update on software licensing agreement.",
        "Request for collaboration on cloud computing project.",
        "Follow-up on the status of the latest software update.",
        "Discussion on potential partnerships with startups in the tech industry.",
        "Reminder: Team meeting at 2pm to discuss project timelines.",
    ]
)

apple = Company(
    name="Apple",
    status="On hold",
    numberOfMeetings="2",
    emails=[
        "Invitation to Apple's annual developer conference.",
        "Discussion on potential partnership opportunities.",
        "Update on the progress of the new product launch.",
        "Reminder: Deadline for submitting app designs is next week.",
        "Request for feedback on the latest iOS update.",
    ]
)

facebook = Company(
    name="Facebook",
    status="Exploratory",
    numberOfMeetings="4",
    emails=[
        "Presentation on ad targeting algorithms.",
        "Interest in joint research on social media trends.",
        "Update on the latest user engagement metrics.",
        "Request for input on the design of the new user interface.",
        "Discussion on potential acquisitions in the tech industry.",
    ]
)

tesla = Company(
    name="Tesla",
    status="Active",
    numberOfMeetings="6",
    emails=[
        "Tesla Model Y delivery update.",
        "Discussion on renewable energy initiatives.",
        "Request for feedback on the latest autopilot software.",
        "Reminder: Deadline for submitting project proposals is approaching.",
        "Update on the progress of the new Gigafactory construction.",
    ]
)
