from langchain_ollama import ChatOllama


def get_llm(json_mode=False):

    kwargs = {
        "model": "llama3.2:3b",
        "temperature": 0,
    }

    if json_mode:
        kwargs["format"] = "json"

    return ChatOllama(**kwargs)