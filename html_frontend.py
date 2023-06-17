from chat_app import ChatApp

class HTMLFrontEnd:
    """
    Class representing the HTML front end.
    """

    def __init__(self):
        """
        Initializes the HTML front end.
        """
        self.chat_app = ChatApp()

    def display_chat(self, chat_history):
        """
        Displays the chat history on the HTML page.
        """
        # Placeholder logic to display the chat history on the HTML page
        pass

    def get_user_input(self):
        """
        Retrieves user input from the HTML form.
        """
        user_input = input("User: ")
        response = self.chat_app.process_input(user_input)
        self.display_chat(self.chat_app.get_from_redis())
        return response
