import os
from dotenv import load_dotenv
from google import genai
import argparse



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

def main():
    print("Hello from aiagent!")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.user_prompt
    )

    usage = response.usage_metadata

    if usage is None:
        raise RuntimeError("No usage metadata returned from API")

    if usage.prompt_token_count == 0:
        raise RuntimeError("Prompt token count is 0 — request likely failed")

    if usage.candidates_token_count == 0:
        raise RuntimeError("Response token count is 0 — model returned no output")

    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    print(response.text)


if __name__ == "__main__":
    main()
