from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def get_temperature(city: str) -> float:
    return 20.0

def main():
    question = input("Your question: ")
 
    prompt = f"""
    You are a helpful assistant that can answer questions about the weather.
    You can use tools if you feel like it.
    - get_temperature(city: str) -> float: Returns the temperature in the given city.

    If you want to use a tool, use the following format:
    tool_name: arg1, arg2, arg3, ...

    Example:
    get_temperature: New York

    If you don't want to use a tool, just answer the question.

    Question: {question}

    If you request a tool, please output ONLY the tool call and nothing else.
    """
 
    response = client.responses.create(
        model="gpt-4o",
        input=prompt,
    )

    reply = response.output_text

    if reply.startswith("get_temperature:"):
        city = reply.split(":")[1].strip()
        temperature = get_temperature(city)
        
        prompt = f"""
        You are a helpful assistant that can answer questions about the weather. 
        Here is the user's question: {question}
        Here is the temperature in the {city}: {temperature}
        """

        response = client.responses.create(
            model="gpt-4o",
            input=prompt,
        )

        reply = response.output_text

        print(reply)
    else:
        print(reply)

print(get_temperature("New York"))



