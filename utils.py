from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Check your .env file.")

def summarize_text(text, template):
    prompt = build_prompt("summarize", text, template)
    return ask_openai(prompt)

def explain_text(text, template):
    prompt = build_prompt("explain", text, template)
    return ask_openai(prompt)

def generate_quiz(text, template):
    prompt = build_prompt("quiz", text, template)
    return ask_openai(prompt)

def build_prompt(task, text, template):
    if task == "summarize":
        if template == "Simple":
            return f"Give a simple and concise summary:\n\n{text}"
        elif template == "Detailed":
            return f"Provide a detailed summary with examples:\n\n{text}"
        elif template == "Bullet Points":
            return f"Summarize the following in bullet points:\n\n{text}"

    if task == "explain":
        if template == "Simple":
            return f"Explain this in simple terms:\n\n{text}"
        elif template == "Detailed":
            return f"Give a detailed explanation with analogies:\n\n{text}"
        elif template == "Bullet Points":
            return f"Explain the content as bullet points:\n\n{text}"

    if task == "quiz":
        if template == "Simple":
            return f"Create 5 basic MCQs:\n\n{text}"
        elif template == "Detailed":
            return f"Create 5 challenging MCQs with 4 options:\n\n{text}"
        elif template == "Bullet Points":
            return f"List 5 quiz-style questions with answers:\n\n{text}"


client = OpenAI()  # Automatically uses OPENAI_API_KEY env variable

def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

