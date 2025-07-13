import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    if len(sys.argv) > 1:
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        contents = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=contents)]),
        ]
        #contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        
        response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        if len(sys.argv) > 2:
            output_level = sys.argv[2]
            if output_level == "--verbose":
                print(f"User prompt: {contents}")
                print(f"Prompt tokens: {prompt_tokens}")
                print(f"Response tokens: {response_tokens}")
        print(response.text)
    else:
        print("no argument was provided")
        sys.exit(1)

if __name__ == "__main__":
    main()
