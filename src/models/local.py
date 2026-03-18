import requests

def ask_model(model, prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        data = response.json()


        if "response" in data:
            return data["response"]


        if "error" in data:
            return f"ERROR: {data['error']}"


        return f"ERROR: invalid format {data}"

    except Exception as e:
        return f"ERROR: {str(e)}"


def ask_llama(prompt):
    return ask_model("llama3", prompt)


def ask_mistral(prompt):
    return ask_model("mistral", prompt)


def ask_phi(prompt):
    return ask_model("phi3", prompt)