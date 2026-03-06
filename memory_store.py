class LongTermMemory:

    def __init__(self):
        self.data = {
            "password reset": "To reset your password, go to settings and click reset password.",
            "internet issue": "Restart the router and check network cables.",
            "email problem": "Check your internet connection and verify SMTP settings.",
            "software installation": "Download the installer from the official website and run setup."
        }

    def search(self, query):

        query = query.lower()

        for key in self.data:
            if key in query:
                return self.data[key]

        return "No relevant information found in memory."

