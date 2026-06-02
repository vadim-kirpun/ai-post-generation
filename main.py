import requests
import os
from openai import OpenAI

load_dotenv()

client = OpenAI()

def generate_post(topic):
    prompt = """
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
    <post>
    <title>How to make a sandwich</title>
    <content>
    A sandwich is a simple meal that can be made with a variety of ingredients.
    </content>
    </post>

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
