REDIS_HOST = "localhost"
REDIS_PORT = "6379"
CONVERSATION_DB = "0" # full input and output conversational history.
PERSONA_DB = "1" # stores persona traits and other key personality data.
MEMORY_DB = "2" # stores keywordized conversational history and key events/topics.
CONTENT_DB = "3" # ingested content, such as PDFs or code.
API_DB = "4" # ingested reference documentation, such as api.
INDEX_NAME = "wiki-index"
VECTOR_FIELD_NAME = "content_vector"
CHAT_MODEL = "gpt-3.5-turbo"
EMBEDDINGS_MODEL = "text-embedding-ada-002"
KEYWORD_MODEL = "text-ada-002"
AI_NAME = "CODEX"

# Set up the base template
SYSTEM_PROMPT = """
You are {AI_NAME}. 
{AI_NAME} Persona is: {persona}
ACT LIKE {AI_NAME}.

You have access to the following tools:
{tools}

Previous conversation history:
{history}

Relevant long term mem: 
{memory}

Relevant content: 
{content}

Reference documentation:
{apidata}

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!
"""


# Build a prompt to provide the original query, the result and ask to summarise for the user
RETRIEVAL_PROMPT = """Use the content to answer the search query the customer has sent. Provide the source for your answer.
If you can't answer the user's question, say "Sorry, I am unable to answer the question with the content". Do not guess.

Search query: 

{SEARCH_QUERY_HERE}

Content: 

{SEARCH_CONTENT_HERE}

Answer:
"""