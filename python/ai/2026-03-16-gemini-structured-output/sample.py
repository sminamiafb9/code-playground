from google import genai
from pydantic import BaseModel, Field


class State(BaseModel):
    narrator: str = Field(description="語り手")
    character: str = Field(description="登場人物")
    state: str = Field(description="状況")
    place: str = Field(description="場所")


prompt = """
{text} から状況を抽出してください。
"""

text1 = """
吾輩わがはいは猫である。名前はまだ無い。
どこで生れたかとんと見当けんとうがつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。
"""[1:-1]

text2 = """
ある日の暮方の事である。
一人の下人が羅生門の下で雨やみを待っていた。
"""

client = genai.Client()

for text in [text1, text2]:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt.format(text=text),
        config={
            "response_mime_type": "application/json",
            "response_json_schema": State.model_json_schema(),
        },
    )

    if response.text is not None:
        state = State.model_validate_json(response.text)
        print(state)
    else:
        print("failed to extract.")
