import requests

def ask_model(model, prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def ask_llama(prompt):
    return ask_model("llama3", prompt)


def ask_mistral(prompt):
    return ask_model("mistral", prompt)


def ask_phi(prompt):
    return ask_model("phi3", prompt)