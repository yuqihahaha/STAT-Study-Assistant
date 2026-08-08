import os

from dotenv import load_dotenv
from openai import OpenAI

# Read the .env file and load the environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def ask_question(notes: str, question: str) -> str:
    """Ask the model to answer a question based on the provided course materials."""

    if not notes.strip():
        raise ValueError("Course materials cannot be empty.")

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    # Create a prompt for the model
    prompt = """
    You are a patient and helpful statistics tutor.

    Answer using the student's provided notes when possible.
    Explain the answer step by step.
    Define mathematical notation clearly.
    Use a simple example when it helps.
    """

    # Call the OpenAI API to get a response
    response = client.responses.create(
        model="gpt-5-mini",
        instructions=prompt,
        input=f"""
        STUDENT NOTES:
        {notes}

        STUDENT QUESTION:
        {question}  
        """, 
    )

    return response.output_text