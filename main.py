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
    add_user_message(messages, "Define Quantum Computing in one sentence.")
    answer = chat(messages)
    add_assistant_message(messages, answer)

    add_user_message(messages, "Write anouther sentence")
    answer2 = chat(messages)
    add_assistant_message(messages, answer2)

    pprint(messages)

if __name__ == "__main__":
    main()
