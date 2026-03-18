from google import genai
from google.genai import types
from pydantic import BaseModel, Field


class Temperature(BaseModel):
    temperature: int = Field(description="気温")
    unit: str = Field(default="Celsius", description="単位")


def get_current_temperature(location: str) -> Temperature:
    """location地点の気温を返します。

    Args:
        location (str): 観測地点

    Returns:
        Temperature: 観測地点の気温
    """
    return Temperature(temperature=24)


def get_current_location() -> str:
    """現在地点を返します。

    Returns:
        str: 現在地点
    """
    return "東京"


client = genai.Client()
config = types.GenerateContentConfig(
    tools=[
        get_current_location,
        get_current_temperature,
    ]
)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents="今の気温は何度でしょうか?",
    config=config,
)

print(response.text)
