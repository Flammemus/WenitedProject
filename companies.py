class Company:
    companyList = []
    def __init__(self, name, status, numberOfMeetings, emails):
        self.name = name
        self.status = status
        self.numberOfMeetings = numberOfMeetings
        self.emails = emails
        Company.companyList.append(self)

# Company attributes are fake and made up

wenited = Company(
    name="Wenited",
    status="Progressing",
    numberOfMeetings="11",
    emails=[
        "Hey! You need to be in a meeting at 10am. We'll be discussing the latest updates on our project milestones and addressing any roadblocks. Your insights are crucial to ensure we stay on track and meet our deadlines.",
        "Remember to make the GoFile feature that we talked about. The one where you need to summarize all emails from a specific company. This feature will significantly enhance our efficiency in managing client communications and streamline our workflow.",
        "Final reminder for the quarterly performance review tomorrow. Please be prepared with your updates. This review is essential for assessing our progress, identifying areas for improvement, and aligning our strategies for the upcoming quarter.",
        "Follow-up on the discussion about expanding into international markets. Can you provide more details? Exploring international expansion opportunities is critical for our company's growth trajectory. Your insights will help us make informed decisions and devise effective strategies.",
        "Action item: Review the latest user feedback and come up with a plan for improvements. Understanding user needs and addressing their feedback promptly is crucial for enhancing customer satisfaction and retaining our user base. Let's work together to implement meaningful improvements.",
    ]
)

amazon = Company(
    name="Amazon",
    status="Slow",
    numberOfMeetings="3",
    emails=[
        "Hey! You need to be in a meeting at 5pm, you have to be there. Very important. In this meeting, we'll be discussing the recent challenges we've faced and brainstorming solutions to overcome them. Your presence and input are valuable for finding effective resolutions.",
        "Please restructure our database for more user-friendly use. Optimizing our database structure will improve data accessibility, enhance system performance, and ensure a smoother user experience. Your expertise in database management will be instrumental in executing this task efficiently.",
        "Update on the latest sales figures. We're seeing a slight decrease in revenue. It's crucial to analyze the factors contributing to this decline and devise strategies to reverse the trend. Your insights can help us identify areas for improvement and implement targeted solutions.",
        "Discussion on potential collaborations with third-party sellers. What are your thoughts? Exploring partnerships with third-party sellers presents opportunities for expanding our product offerings and reaching new customer segments. Your input on potential collaborators and partnership models is valuable for evaluating these opportunities.",
        "Reminder: Deadline for submitting project proposals is approaching. Make sure to finalize yours. Submitting comprehensive project proposals is essential for securing resources and approval for your initiatives. Let's ensure we meet the deadline and present compelling proposals.",
    ]
)

google = Company(
    name="Google",
    status="Active",
    numberOfMeetings="8",
    emails=[
        "Reminder: Quarterly review meeting tomorrow. The quarterly review meeting provides an opportunity to reflect on our achievements, discuss challenges, and align our strategies for the next quarter. Your participation and insights are crucial for ensuring our continued success.",
        "Proposal for new AI-driven project. We're proposing an exciting new project leveraging AI technology to enhance user experience and drive innovation. Your expertise in AI and creative ideas will be valuable for shaping this project and maximizing its impact.",
        "Update on the latest developments in machine learning algorithms. Staying updated on the latest advancements in machine learning is essential for maintaining our competitive edge and driving innovation in our products and services. Let's discuss how we can leverage these developments in our projects.",
        "Request for feedback on the beta version of our new software. Your feedback on the beta version is invaluable for identifying any bugs or usability issues and ensuring a smooth launch. Let's collaborate to provide comprehensive feedback and optimize the user experience.",
        "Invitation to a webinar on cloud computing trends. Don't miss out! The webinar will provide insights into the latest trends and best practices in cloud computing, which are crucial for our ongoing projects and future initiatives. Let's attend together to stay ahead of the curve.",
    ]
)

microsoft = Company(
    name="Microsoft",
    status="Stalled",
    numberOfMeetings="5",
    emails=[
        "Update on software licensing agreement. We've made significant progress in negotiating the terms of the software licensing agreement. Your input on key clauses and licensing models is critical for finalizing the agreement and ensuring it aligns with our business objectives.",
        "Request for collaboration on cloud computing project. We're exploring opportunities for collaboration on a cloud computing project that aligns with your expertise. Your involvement in this project can significantly enhance its success and impact. Let's discuss further details and potential contributions.",
        "Follow-up on the status of the latest software update. Ensuring timely delivery of software updates is crucial for addressing user feedback and maintaining product reliability. Your update on the status of the latest update will help us track progress and anticipate any potential delays.",
        "Discussion on potential partnerships with startups in the tech industry. Exploring partnerships with startups presents opportunities for innovation and market expansion. Your insights on potential partners and collaboration models will be valuable for evaluating these opportunities.",
        "Reminder: Team meeting at 2pm to discuss project timelines. The team meeting is essential for aligning our efforts, addressing any bottlenecks, and ensuring we meet our project deadlines. Your participation is crucial for effective coordination and successful project delivery.",
    ]
)

apple = Company(
    name="Apple",
    status="On hold",
    numberOfMeetings="2",
    emails=[
        "Invitation to Apple's annual developer conference. The developer conference offers insights into the latest technologies and best practices for app development on Apple platforms. Your attendance at this event can inspire new ideas and enhance your skills.",
        "Discussion on potential partnership opportunities. Exploring partnership opportunities presents avenues for innovation and growth. Your input on potential partners and collaboration strategies is valuable for identifying mutually beneficial opportunities.",
        "Update on the progress of the new product launch. We've made significant progress in the development of our new product. Your update on the project status and any challenges encountered will help us address any roadblocks and ensure a successful launch.",
        "Reminder: Deadline for submitting app designs is next week. Submitting your app designs by the deadline is crucial for review and feedback. Let's ensure we meet the deadline to facilitate timely iterations and improvements.",
        "Request for feedback on the latest iOS update. Your feedback on the latest iOS update is invaluable for identifying any bugs or usability issues and ensuring a seamless user experience. Let's collaborate to provide comprehensive feedback and enhance the quality of our products.",
    ]
)

facebook = Company(
    name="Facebook",
    status="Exploratory",
    numberOfMeetings="4",
    emails=[
        "Presentation on ad targeting algorithms. The presentation will delve into the latest advancements in ad targeting algorithms and their impact on advertising effectiveness. Your attendance will provide valuable insights for optimizing our advertising strategies.",
        "Interest in joint research on social media trends. Collaborating on joint research projects presents opportunities for knowledge sharing and innovation. Your expertise in social media trends can contribute significantly to the success of this initiative.",
        "Reminder: Deadline for submitting app designs is next week. Submitting your app designs by the deadline is crucial for review and feedback. Let's ensure we meet the deadline to facilitate timely iterations and improvements.",
        "Request for feedback on the latest iOS update. Your feedback on the latest iOS update is invaluable for identifying any bugs or usability issues and ensuring a seamless user experience. Let's collaborate to provide comprehensive feedback and enhance the quality of our products.",
    ]
)