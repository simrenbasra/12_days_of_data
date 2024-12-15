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

    # First include inputs of user:
    prompt = f'Write a {genre} short story about a {char_type}.'

    # Tailoring prompt depending on genre 
    if genre.lower() in ('comedy', 'romcom', 'romantic comedy'):
        prompt += 'Introduce a humourous and playful twist'
    elif genre.lower() == 'action':
        prompt += 'Story should be fast-paced with thrilling events to keep readers engaged.'
    elif genre.lower() in ('romance', 'romcom', 'romantic comedy'):
        prompt += 'Stroy should focus on heartwarming and emotional connections between characters.'
    elif genre.lower() == 'horror':
        prompt += 'Introduce suspense and eerie events to spook readers but still keep to a Christmas theme.'
    elif genre.lower() == 'msytery':
        prompt += 'Introduce clues and unexpected turns in the plot while keeping to a Christmas theme.'
    elif genre.lower() == 'fantasy':
        prompt += 'Set the story in imaginative placces and incoporate some festive magic.'
    else:
        prompt += 'The one of the story should be uplifting and festive.'

    # To ensure the story starts off strong and engages the reader
    prompt += 'Start with a strong, compelling hook to immediately engage the reader.'

    # To build out the story, adding in other Christmas Characters and ensure characters develop with the story
    prompt += 'Include other Christmas characters with distinct roles to support the main story, without overshadowing it.'
    prompt += 'Develop relateble characters who show development and growth or learn a lesson as the story develops.'

    # Story plot
    prompt += 'Story must have a clear, logical flow where plots connect naturally and seamlessly.'
    prompt += 'The story should have a realistic yet imaginative plot that shows creativity while also being believable.'
    prompt += 'The end of the story should tie all subplots to the main plot, show resolution with a clear lesson.'

    # Langauge 
    #prompt += 'Use simple, clear language that is suitable for all ages. Do not use overly complex or uncommon words.'
    prompt += 'Use simple, descriptive language to make the story and characters come alive, while avoiding overly complicated terms/words.'


    return prompt

#####################################################
# Get response from model for a given prompt
#####################################################
def get_response(prompt):

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative author writing short Christmas themed stories, all stories should be 400 words. Your stories are known for their creative, unexpected plot twists"},
            {"role": "user", "content": prompt}
        ]

    )

    return(completion.choices[0].message.content)

