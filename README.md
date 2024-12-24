# 12 Days of Data

## Project Objective 
With Christmas approaching, I wanted my project to have a festive theme! The aim of this project is to generate short, tailored Christmas stories using a Large Language Model (LLM).

The idea is for users to input story details such as characters and genre. The LLM will process this input to produce a personalised Christmas story.

The aim is to build this project in 12 days!

## Getting Started 
To make things easier for me, I’ve decided to plan out a few things before diving into the project. This includes selecting the LLM I will use, determining user inputs, defining the expected output and decide how best to evaluate the model’s performance. By clarifying these points ahead of time, I’ll be ready to hit the ground running!

#### **LLM**
**1. Data Collection**

Collecting a large, high-quality dataset of Christmas-themed short stories is time-consuming. To fine-tune a model effectively, I would need at least 100 examples for meaningful results.

All data must come from publicly available or open-source datasets to avoid copyright infringement. This makes data collection even more challenging and time consuming.

Prompt engineering does not require any training data. This frees up my time to focus on designing prompts that leverage GPT 4’s full capabilities to get the best output.

I considered using GPT to generate training data for a generative model, but this felt counterproductive. I thought using GPT-4 with prompt engineering, would deliver better outputs rather than using GPT-generated data to train another generative AI model.

GPT-4’s creativity and ability to generate text make it well-suited for this project without additional fine-tuning.

**2. Time**

Fine-tuning a large generative model can be both computationally expensive and time-consuming.

With a tight 12-day timeline, fine-tuning a model (including data collection) would likely take more than 12 days.

Using GPT-4 allows me to start generating stories almost immediately.

Overall, GPT-4 seems to be the more suitable choice for this project due to the model’s ability to generate creative text without the need for fine-tuning. By combining GPT-4 with effective prompt engineering, I believe the results can still achieve a high level of quality.

#### **Inputs**
For this project, LLM will generate short Christmas stories based on user-provided inputs. Here’s a breakdown of details users can provide to personalise their story:

**Mandatory Inputs:**

- Character Type: Choose a classic Christmas Character (Santa, Elf, Reindeer, etc)

- Genre: Choose genre of story (action, comedy, etc)

**Optional Inputs:**

- Moral: Key takeaway from the story (giving, kindness, etc)

- Location: Main setting of the story (North Pole, Santas Workshop, etc)

The goal of this project is to test the LLM’s creative abilities, so I intentionally kept mandatory inputs to a minimum. The fewer details the user provides, the more the LLM has to generate itself, allowing it to demonstrate creativity in creating stories. Minimum inputs would also test my ability to create meaningful prompts. The optional inputs allow users to further customise their stories.

#### **Expected Output**
- **Length:** To be determined by the user, between 300 words and 1000 words.

- **Cohesiveness:** The generated story should be logical with a clear flow from beginning to end.

- **User Inputs:** The story should include and reflect all the inputs provided by the user.

- **Creativity**: The story should show creativity in character profiles and storylines.

- **Response Time:** The LLM should be able to create high-quality outputs within a reasonable time.


## Sharing Updates
Every three days, I shared my progress as part of my project, to view [visit my blog post](https://simrenbasra.github.io/simys-blog/2024/12/12/12_days_of_data_diary.html).


## Instructions to Run the Project

1. Clone the Repository: 

    Enter the following command in terminal:

    `https://github.com/simrenbasra/12_days_of_data.git`

2. Navigate to project directory (where you cloned project to)

3. Set up Environmnet using requirements.txt

    I find it best to set up a new environmnet for each project:

    `conda create --name xxxx python 3.9`
    `conda activate xxxx`

4. Install project required libraries

    `pip install -r requirements.txt`

5. Navigate to notebooks/02_streamlit and run Streamlit App

    `streamlit run app.py`

