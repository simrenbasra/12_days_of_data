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
    if genre.lower() == 'comedy':
        prompt += 'Introduce humourous mishaps and playful twists into the story.'
        prompt += 'The story should focus on comedic situation while keeping the the festive theme.'
    elif genre.lower() == 'action':
        prompt += 'Story to be fast-paced with thrilling chases or rescues, set against the backdrop of Christmas.'
    elif genre.lower() == 'romance':
        prompt += 'Story to be centred on the emotional connection and blossoming romance between two characters.'
    elif genre.lower() == 'horror':
        prompt += 'Create suspense with eerie twists and unsettling events to spook readers while keeping to a Christmas theme.'
    elif genre.lower() == 'mystery':
        prompt += 'Create suspense by incorporating cryptic clues and unexpected turns for a Christmas themed mystery.'
    elif genre.lower() == 'fantasy':
        prompt += 'Set the story in imaginative places filled with whimsical creatures and magical objects.'
    elif genre.lower() == 'sci-fi':
        prompt += 'Blend futuristic technology and AI with a festive twist.'
        prompt += 'To incorporate space travel or time travel in a Christmas-themed adventure.'
    else:
        prompt += 'The overall tone of the story should be uplifting and festive.'

    # To ensure the story starts off strong and engages the reader
    prompt += "Start with a strong hook or surprising event to grab the reader's attention."

    # To build out the story, adding in other Christmas Characters and ensure characters develop with the story
    prompt += 'Develop relateble characters who show development and growth or learn a lesson as the story develops.'
    prompt += 'Show how Chrsitmas spirit influences the characters and drives them to succeed'

    # Story plot
    prompt += 'Include creative and realistic twists that make the story fun and believable.'
    prompt += 'Make the story have a clear logical flow of events.'

    # Langauge 
    prompt += 'Use simple, descriptive language to describe events, emotions and characters to make the story come alive.'
    prompt += 'Make the story suitable for all ages by avoiding overly complex or uncommon words.'

    return prompt

#####################################################
# Get response from model for a given prompt
#####################################################
def get_response(prompt, story_len):

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"You are a creative author writing short Christmas themed stories. Ensure the story is exactly {story_len} words long, has a title and uses UK English spelling. Your stories are known for their creative, unexpected plot twists"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1800 #max tokens includes in and out

    )

    return(completion.choices[0].message.content)

 