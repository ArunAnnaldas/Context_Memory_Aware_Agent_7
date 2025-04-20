from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.callbacks import get_openai_callback

# Initialize memory
memory = ConversationBufferMemory(memory_key="history", return_messages=True)

# Shared LLM
llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo",
    openai_api_key=""
)

# Create memory-aware ConversationChain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

def run_memory_agent():
    print("\n Memory-Aware Multi-Turn Task")

    # Prompt 1
    input_1 = "Write a Python function to reverse a string"
    print(f"\n User: {input_1}")
    response_1 = conversation.predict(input=input_1)
    print(f" Assistant:\n{response_1}")

    # Prompt 2 (Relies on memory of first response)
    input_2 = "Now write a function that uses the previous one to check for a palindrome"
    print(f"\n User: {input_2}")
    response_2 = conversation.predict(input=input_2)
    print(f" Assistant:\n{response_2}")

    # Show stored memory (optional)
    print("\n Current Memory History:")
    print(memory.load_memory_variables({})["history"])

# 🔍 Run it with token tracking
if __name__ == "__main__":
    with get_openai_callback() as cb:
        run_memory_agent()
        print("\n Token Usage Summary:")
        print(cb)
