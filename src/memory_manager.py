from langchain_classic.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_buffer_memory():
    memory = ConversationBufferMemory(memory_key="chat_history",
                              return_messages=True)
    return memory
    
def get_window_memory(window_size):
    memory = ConversationBufferWindowMemory(chat_memory="chat_history",
                                            return_messages=True,
                                            k=window_size) 
    return memory
