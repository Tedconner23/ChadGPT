from chat_app import ChatApp

class PythonBackend:
    """
    Class representing the Python backend.
    """

    def __init__(self):
        """
        Initializes the Python backend.
        """
        self.chat_app = ChatApp()

    def start_server(self):
        """
        Starts the Python backend server.
        """
        while True:
            request = input("Enter a request: ")
            response = self.process_request(request)
            print(response)

    def process_request(self, request):
        """
        Processes the user request and returns a response.
        """
        response = self.chat_app.process_input(request)
        return response
