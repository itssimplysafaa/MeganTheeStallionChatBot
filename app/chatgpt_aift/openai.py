from dotenv import load_dotenv 
import openai 
import os 

load_dotenv()

openai.api_key = os.getenv('CHATGPT_KEY')

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-1106:personal:megantheestallion4:9Ahl884w",
        prompt=prompt,
        temperature=.9,
        max_tokens=150
    )

    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response