import os
from google import genai
from google.genai import types

# Initialize the Gemini client
# Ensure GEMINI_API_KEY is set in your environment variables
client = genai.Client()

def ask_edugenie(prompt: str, system_instruction: str = None) -> str:
    """Generates a response using the Gemini 2.5 Flash model."""
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.7,
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config,
    )
    return response.text

if __name__ == "__main__":
    system_prompt = (
        "You are EduGenie, an interactive AI learning assistant. "
        "Your goal is to break down complex topics into clear, easy-to-understand explanations with examples."
    )
    
    user_query = "Can you explain how photosyntehsis works in simple terms?"
    
    print("Asking EduGenie...\n")
    answer = ask_edugenie(prompt=user_query, system_instruction=system_prompt)
    print(answer)
