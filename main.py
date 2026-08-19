from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from pprint import pprint

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"


def add_user_message(messages, content):
    user_message = {"role": "user", "content": content}
    messages.append(user_message)
    return messages

def add_assistant_message(messages, content):
    assistant_message = {"role": "assistant", "content": content}
    messages.append(assistant_message)
    return messages 

def chat(messages):
    response = client.messages.create(
        model=model,
        max_tokens=100,
        messages=messages,
    )
    return response.content[0].text

def main():

    messages = []
    exit_commands = ["exit", "quit", "bye"]
    is_exit = False
    while not is_exit:
        user_input = input("User: ")

        if user_input in exit_commands:
            exit_message = "Goodbye! Have a great day!"
            print(f"Assistant: {exit_message}")
            is_exit = True
            exit(0)
        messages = add_user_message(messages, user_input)
        assistant_response = chat(messages)
        messages = add_assistant_message(messages, assistant_response)
        print("---")
        print(f"Assistant: {assistant_response}")
        print("---")

if __name__ == "__main__":
    main()
