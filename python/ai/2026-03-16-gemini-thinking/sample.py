from google import genai
from google.genai import types

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

question = """
りんごを3個持っています。

そのうち2個を食べました。
さらに友人から3個もらいました。
そのあと1個食べました。

今、あなたはいくつのりんごを持っていますか？
"""[1:-1]

levels = [
    types.ThinkingLevel.MINIMAL,
    types.ThinkingLevel.LOW,
    types.ThinkingLevel.MEDIUM,
]

for level in levels:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        config=types.GenerateContentConfig(
            system_instruction="簡潔に答えてください。",
            thinking_config=types.ThinkingConfig(thinking_level=level),
        ),
        contents=question,
    )
    print("results:")
    print(f"{level = }")
    print(f"{response.text = }")

    if (
        response.usage_metadata is not None
        and response.usage_metadata.thoughts_token_count is not None
    ):
        thoughts_token_count = response.usage_metadata.thoughts_token_count
        print(f"{thoughts_token_count = }")
    else:
        print("thoughts_token_count is not exists.")
    print()
