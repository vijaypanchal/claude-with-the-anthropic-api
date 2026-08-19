from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from pprint import pprint

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"


def main():

    respose = client.messages.create(
        model=model,
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": "Write is quantum computing ? Answer in one line",
            }
        ],
    )

    pprint(respose.content[0].text)

    respose2 = client.messages.create(
        model=model,
        max_tokens=100,
        messages=[{"role": "user", "content": "Write one more line"}],
    )

    pprint(respose2.content[0].text)


if __name__ == "__main__":
    main()
