#####################################################
# Imports
#####################################################
from dotenv import load_dotenv
import os
from openai import OpenAI

#####################################################
# Load and access API Key securely
#####################################################
# Use `dotenv` to load API, pass in .env file where api key is securely stored
load_dotenv(dotenv_path="../01_set_up/API_key.env")

# Access the API key using os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#####################################################
# Build prompt given inputs from user 
#####################################################
def build_prompt(char_type, genre):

    prompt = f'Write a {genre} story about a {char_type}'

    return prompt

#####################################################
# Get response from model for a given prompt
#####################################################
def get_response(prompt):

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an author of short Christmas themed stories ranging from 500 words to 1000 words. Your stories are known for their creative, unexpected plot twists"},
            {"role": "user", "content": prompt}
        ]
    )

    return(completion.choices[0].message.content)

