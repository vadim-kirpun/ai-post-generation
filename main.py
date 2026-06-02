import requests
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
EXAMPLES_PATH = Path(__file__).with_name("post_examples.json")


def format_examples(examples):
    return "\n\n".join(
        f"<post>\n<title>{item['title']}</title>\n<content>\n{item['content']}\n</content>\n</post>"
        for item in examples
    )

def generate_post(topic):
    examples_data = json.loads(EXAMPLES_PATH.read_text(encoding="utf-8"))
    examples = format_examples(examples_data)
    
    prompt = f"""
    You are a helpful assistant that generates posts for a social media platform.
    The user will provide you with a topic, and you will generate a post about it.
    The post should be 100 words long.
    The post should be in the following format:
    <post>
    <title>
    <content>
    </post>

    <topic>
    {topic}
    </topic>

    Here are some examples of posts:
    {examples}

    Please use the tone, language, and style of the examples to generate the post. Don't use the same words or phrases as the examples.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    return response.output_text

def main():
    user_input = input("What should the post be about? ")
    post = generate_post(user_input)
    print(post)

if __name__ == "__main__":
    main()
