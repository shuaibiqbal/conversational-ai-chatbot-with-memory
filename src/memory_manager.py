from langchain_classic.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_buffer_memory():
    memory = ConversationBufferMemory(memory_key="chat_history",
                              return_messages=True)
    return memory
    
def get_window_memory(window_size):
    memory = ConversationBufferWindowMemory(memory_key="chat_history",
                                            return_messages=True,
                                            k=window_size) 
    return memory

if __name__ == "__main__":
    window_size = 2
    if window_size is not None:
        memory = get_window_memory(window_size)
    else:
        memory = get_buffer_memory()
    memory.save_context(
        {"input":"Hi"},
        {"output": "Hello!"}
    )
    memory.save_context(
        {"input": "my name is shuaib"},
        {"output": "nice to meet you"}
    )
    memory.save_context(
        {"input":"I love Ai"},
        {"output": "AI is Amazing"}
    )
    print(memory.load_memory_variables({}))