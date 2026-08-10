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
    You are a beginner-friendly statistics tutor.

    Answer using the student's provided notes when possible.
    Explain the answer step by step.
    Keep the response concise, usually under 400 words.
    Use examples only when helpful.

    Formatting rules:
    - Write normal explainations using Markdown.
    - Use $...$ for inline mathematical expression.
    - Use $$...$$ for equations that should appear on their own line.
    - Never use \\[ ... \\] for equations.
    - Never display raw LaTex commands outside of $...$ or $$...$$.
    - Use Markdown headings and bullet points when helpful.
    - Make the response easy for a student to read.
    """

    # Call the OpenAI API to get a response
    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions=prompt,
        input=f"""
        STUDENT NOTES:
        {notes}

        STUDENT QUESTION:
        {question}  
        """, 
    )

    return response.output_text