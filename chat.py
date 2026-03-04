from ollama import chat
from dotenv import load_dotenv
import os
load_dotenv()


def ask_sre_question():
    model = os.getenv("MODEL","llama3.1:8b")
    
    prompt = input("Ask your question:")
    
    try:
        response = chat(model=model,messages=[
            {
                'role': 'user',
                'content': prompt,
            }])
        print(f"--- SRE Response ---\n")
        print(response.message.content)
    except Exception as e:
        print(f"Error communicating with ollama: {e}")
        
if __name__ == "__main__":
    ask_sre_question()