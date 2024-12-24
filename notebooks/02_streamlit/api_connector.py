#####################################################
# Imports
#####################################################
from dotenv import load_dotenv
import os
from openai import OpenAI
import random

#####################################################
# Load and access API Key securely
#####################################################
# Use `dotenv` to load API, pass in .env file where api key is securely stored
load_dotenv(dotenv_path="../01_set_up/API_key.env")
# Access the API key using os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#####################################################
# FUNCTION: Random Selection
#####################################################
def rand_choice():
    """
    Description: 
        To randomly assign values for all input fields (character type, genre, location and theme).

    Inputs: 
        No inputs.

    Ouputs: 
        Returns a tuple of 4 elements.
        Each element is a random value for all inputs: character type, genre, location and theme.
    """

    # using random.choice to set the values randomly from a list of values (same for all inputs)
    char_type = random.choice(['Elf', 'Reindeer', 'Santa', 'Snowman', 
                              'Gingerbread Man', 'Grinch', 'Mrs Claus',
                              'Angel'])
    genre = random.choice(['Comedy', 'Action', 'Fantasy', 'Horror', 'Romance', 'Sci-Fi', 'Mystery'])
    location = random.choice(['Lapland', 'London', 'North Pole', 'New York', 'Ice Castle', 'Paris'])
    theme = random.choice(['Generosity', 'Courage', 'Kindness', 'Togetherness',
                            'Hope', 'Forgiveness', 'Patience','Empathy', 'Gratitude' ])
    
    return (char_type, genre, location, theme)

#####################################################
# FUNCTION: Builds Prompts
#####################################################
def build_prompt(char_type, genre, location, theme):
    """
    Description: 
        To build prompts to pass into the model.
        Prompts are tailored to user inputs: character type, genre, location and theme

    Inputs: 
        character type - string
        genre - string
        location - string
        theme - string

    Ouputs: 
        Returns a string, a single prompt to be passed to the model.
    """
    # Stating genre of the story and type of character
    prompt = f'Write a {genre} short story about a {char_type}.'

    # Tailoring prompt depending on genre 
    if genre.lower() == 'comedy':
        prompt += 'The story should feature slapstick humour with playful twists.'
        prompt += 'The characters should be hilariously quirky, getting into ridiculous situations.'
    elif genre.lower() == 'action':
        prompt += 'Story to be fast-paced and action-packed with thrilling chases or rescues.'
        prompt += 'Insert moments of tension into the story to excite readers.'
    elif genre.lower() == 'romance':
        prompt += 'Story to be centred on the emotional connection and blossoming romance between two characters.'
    elif genre.lower() == 'horror':
        prompt += 'Create a chilling story with eerie twists and unsettling events to spook readers.'
        prompt += 'Create suspense by using vivid descriptions and create tension to further spook readers.'
    elif genre.lower() == 'mystery':
        prompt += 'Create a clever and unexpected mystery that captures the curiosity of readers.'
        prompt += 'Incorporate subtle but challenging cryptic clues and surprising twists into the story.'
    elif genre.lower() == 'fantasy':
        prompt += 'Set the plot in a magical place filled with whimsical creatures and magical objects.'
        prompt += 'Describe the setting or location in rich detail, including magical objects that are in the story.'
        prompt += 'Create a plot to capture the readers imagination incorporate challenging riddles or puzzles into the plot.'
    elif genre.lower() == 'sci-fi':
        prompt += 'Blend futuristic technology and AI with a festive twist.'
        prompt += 'Describe the setting or location in rich detail, including technical concepts that are in the story.'
        prompt += 'To incorporate space travel or time travel into the adventure.'
    else:
        prompt += 'The overall tone of the story should be uplifting and festive.'

    # Include inputs location and theme if provided
    if location:
        prompt +=f'Set the story in {location}.'
    if theme:
        prompt += f'The theme of the story is {theme}.'

    # To ensure the story starts off strong and engages the reader
    prompt += "Start with a strong hook or surprising event to grab the reader's attention."
    
    # prompts controlling character development 
    prompt += 'Develop well-rounded, relatable characters who communicate with each other as the story unfolds.'
    prompt += 'Make sure the main character has a personal goal or challenge to overcome.'
    prompt += 'Explain the characters past experiences as motivation for their actions.'

    # prompts controlling story plot and flow
    prompt += 'Balance imaginative and creative stories with realistic character actions.'
    prompt += 'Design a well structured plot with a clear beginning, middle and end while ensuring there is a logical flow of events.'
    prompt += 'Connect subplots together to the main plot seamlessly.'
    prompt += 'The end of the story should serve as a short reflection summarising lessons learnt from characters.'

    # prompts setting langauge
    prompt += 'Use simple and accessible language to describe events, emotions and characters to make the story come alive.'
    prompt += 'Make the story suitable for all ages by avoiding overly complex or uncommon words.'

    return prompt

#####################################################
# FUNCTION: Retrieves Response from model
#####################################################
def get_response(prompt, story_len):
    """
    Description: 
        To get response from the GPT model after passing in a prompt.

    Inputs: 
        prompt - string
        story_len - int

    Ouputs: 
        Returns a story tailored to user inputs.
    """
    # connect to OpenAI
    client = OpenAI()
    # connect to the chat.completions endpoint and create a new request
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            # assigning role of model to be a writer of stories and define length of stories
            {"role": "system", "content": f"You are a creative author writing short Christmas themed stories. Ensure the story is exactly {story_len} words long, has a title and uses UK English spelling. Your stories are known for their creative, unexpected plot twists"},
            # passing in prompt to model
            {"role": "user", "content": prompt}
        ],
        # model paramters
        #   max_tokens: total tokens passed in and out of the model so this would be length output + lenght of prompt (~800)
        #   temperature: controls creativity and randomness in the output. Value of 0.9 ensures creativity is in the story with intresting twists. 
        max_tokens= story_len + 800,
        temperature = 0.9
    )
    
    return(completion.choices[0].message.content)

 