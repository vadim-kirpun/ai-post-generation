import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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
    """

    payload = {
        "model": "gpt-4o-mini",
        "input": user_input,
    }

    response = requests.post(
        "https://api.openai.com/v1/responses",
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
    )

    return response.json().get("output", [{}])[0].get("content", [{}])[0].get("text", "")

def main():
    user_input = input("What should the post be about? ")
    post = generate_post(user_input)
    print(post)

if __name__ == "__main__":
    main()
