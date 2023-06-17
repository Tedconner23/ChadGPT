from chat_app import ChatApp
from html_frontend import HTMLFrontEnd
from python_backend import PythonBackend
from redis_vector import RedisVectorDatabase, EmbeddingModel

class Main:
    """
    Class representing the main application.
    """

    def __init__(self):
        """
        Initializes the main application.
        """
        self.chat_app = ChatApp()
        self.html_frontend = HTMLFrontEnd()
        self.python_backend = PythonBackend()
        self.redis_db = RedisVectorDatabase()
        self.embedding_model = EmbeddingModel()

    def run(self):
        """
        Runs the main application, creating instances of the necessary classes.
        """
        self.html_frontend.display_chat(self.chat_app.get_from_redis())
        self.python_backend.start_server()

    def update_chat_history(self, input_text, response):
        """
        Updates the chat history with the user input and response.
        """
        self.chat_app.save_to_redis(input_text, response)

    def get_previous_chat_history(self):
        """
        Retrieves the previous chat history from the Redis vector database.
        """
        previous_data = self.redis_db.get_vector()
        return previous_data
