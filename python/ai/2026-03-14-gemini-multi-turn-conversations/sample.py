from google import genai
from google.genai import types

client = genai.Client()
chat = client.chats.create(
    config=types.GenerateContentConfig(system_instruction="簡潔に答えてください。"),
    model="gemini-3.1-flash-lite-preview",
)

prompts = ["富士山の高さは?", "東京スカイツリーは?"]
for i, prompt in enumerate(prompts):
    print(f"[{i}] >> ", prompt)
    response = chat.send_message(prompt)
    print(f"[{i}] << ", response.text)


for message in chat.get_history():
    if message.role is not None:
        print(f"{message.role = }")
    if message.parts is not None:
        print(f"{message.parts[0].text = }")
