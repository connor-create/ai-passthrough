from enum import Enum

class Models(Enum):
    OPENAI = "openai"
    # REMOVE_BG = 1
    # MIDJOURNEY = 2

def query_model(model: Models, query_string: str):
    return "Hello World"