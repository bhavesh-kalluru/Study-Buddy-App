# StudyBuddyApp

StudyBuddyApp is an AI-powered study assistant that helps you learn faster and smarter by summarizing PDFs, generating quizzes, providing explanations, and converting documents into editable formats. It’s designed to enhance your study sessions and make complex materials easier to understand.

---

## Features

- **PDF Upload & Summarization**  
  Upload PDF files and get concise summaries highlighting the key points.

- **Quiz Generation**  
  Automatically generate quizzes from your study materials to test your knowledge.

- **Detailed Explanations**  
  Get AI-generated explanations of complex topics extracted from your documents.

- **Document Conversion**  
  Convert PDFs into editable Word documents for further editing and notes.

- **User-Friendly Interface**  
  Clean and intuitive UI designed to keep you focused and efficient.

- **Cross-Platform Ready**  
  Can be deployed on the web using Streamlit or Flask for access anywhere.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bhavesh-kalluru/StudyBuddyApp.git
   cd StudyBuddyApp
(Optional but recommended) Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file in the project root directory and add your OpenAI API key:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
Usage
To run the app locally with Streamlit:

bash
Copy
Edit
streamlit run app.py
Open your web browser and go to http://localhost:8501 to access the StudyBuddyApp interface.

