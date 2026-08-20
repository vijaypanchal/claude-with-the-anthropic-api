from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from pprint import pprint

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"
system_prompt ="""
You are patient math tutor. 
You will help the user with their math questions, providing clear explanations and step-by-step solutions. 
If the user asks for a specific type of math problem, you will provide an example and guide them through the solution process. 
Always encourage the user to ask questions if they need further clarification.
"""


def add_user_message(messages, content):
    user_message = {"role": "user", "content": content}
    messages.append(user_message)
    return messages

def add_assistant_message(messages, content):
    assistant_message = {"role": "assistant", "content": content}
    messages.append(assistant_message)
    return messages 

def chat(messages):
    response_text = ""
    with client.messages.create(
        model=model,
        max_tokens=100,
        messages=messages,
        system=system_prompt,
        temperature=0.7, 
        stream=True
    ) as stream:
        print("Assistant: ")
        for event in stream:
            if event.type == "content_block_delta":
                text = event.delta.text
                print(text, end="", flush=True)
                response_text += text
    return response_text


def chat_main():

    messages = []
    exit_commands = ["exit", "quit", "bye"]
    is_exit = False
    while not is_exit:
        user_input = input("User: ")

        if user_input in exit_commands:
            exit_message = "Goodbye! Have a great day!"
            print(f"Assistant: {exit_message}")
            is_exit = True
            continue
        messages = add_user_message(messages, user_input)
        assistant_response = chat(messages)
        messages = add_assistant_message(messages, assistant_response)
        #print("---")
        #print(f"Assistant: {assistant_response}")
        #print("---")
       
def stream_main():
    messages = []
    add_user_message(messages, "Hello! is LLM ?")
    with client.messages.create(
        model=model,
        max_tokens=500,
        messages=messages,
        stream=True,
        temperature=0.7,
    ) as stream:
        for event in stream:
            if event.type == "content_block_delta":
                print(event.delta.text, end="", flush=True)
            
def structure_main():
    messages = []
    add_user_message(messages, "Generate a very small event bridge rule as JSON?")
    add_assistant_message(messages, "```json");
    chat(messages)
    pprint(messages)

if __name__ == "__main__":
    #stream_main()
    #chat_main()
    structure_main()
