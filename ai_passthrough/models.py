from enum import Enum
import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class Models(Enum):
    OPENAI = "openai"
    # REMOVE_BG = 1
    # MIDJOURNEY = 2

def openai_query(
        query_string: str,
        checkpoint: str = "text-davinci-003",
        temperature: float = 0.7,
        max_tokens: int = 256,
        top_p: float =  1,
        frequency_penalty: float = 0,
        presence_penalty: float = 0
    ):
        return openai.Completion.create(
            model=checkpoint,
            prompt=query_string,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )

def query_model(model: Models, query_string: str):
    if model == Models.OPENAI:
        response = openai_query(query_string)
        return response.choices[0].text.lstrip()