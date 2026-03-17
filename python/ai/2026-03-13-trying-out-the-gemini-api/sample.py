from google import genai
from google.genai import types

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    config=types.GenerateContentConfig(system_instruction="簡潔に答えてください。"),
    contents="富士山の高さは?",
)
print(response.text)
