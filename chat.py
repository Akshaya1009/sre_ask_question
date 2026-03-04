import os
import argparse
import logging
from ollama import chat
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
load_dotenv()

def analyze_incident(data):
    model = os.getenv("MODEL", "llama3")
    system_message = {
        'role': 'system',
        'content': "You are an expert SRE. Analyze the data for Root Cause and suggest a Fix."
    }
    
    try:
        response = chat(model=model, messages=[system_message, {'role': 'user', 'content': data}])
        print(f"\n--- SRE REPORT ---\n{response.message.content}")
    except Exception as e:
        logging.error(f"Analysis failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI SRE Diagnostic Tool")
    # NEW FEATURE: Added choice between raw string or file path
    parser.add_argument("--logs", type=str, help="Raw log string")
    parser.add_argument("--file", type=str, help="Path to a log file to analyze")
    
    args = parser.parse_args()

    # Feature Logic: Decide where to get the data from
    if args.file:
        if os.path.exists(args.file):
            with open(args.file, 'r') as f:
                log_data = f.read()
            analyze_incident(log_data)
        else:
            logging.error(f"File not found: {args.file}")
    elif args.logs:
        analyze_incident(args.logs)
    else:
        logging.error("Please provide either --logs or --file")
