from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from anthropic import Anthropic
from pprint import pprint


def main():
    client = Anthropic()
    model="claude-sonnet-5"
    respose = client.messages.create(
        model=model,
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": "Write is quantum computing ? Answer in one line"
            }
        ]
    )

    #pprint(respose)
    pprint(respose.content[0].text)   




if __name__ == "__main__":
    main()
