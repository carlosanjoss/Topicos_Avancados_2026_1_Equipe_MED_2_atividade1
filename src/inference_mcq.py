import os
import json
import time
from models.local import ask_llama, ask_mistral, ask_phi


def load_prompt():
    with open("prompts/mcq_prompt.txt", encoding="utf-8") as f:
        return f.read()


def format_options(options):
    return "\n".join([f"{k}) {v}" for k, v in options.items()])


def safe_call(fn, prompt):
    try:
        response = fn(prompt)

        if not isinstance(response, str):
            return "ERROR: invalid response"

        if "error" in response.lower():
            return f"ERROR: {response}"

        return response.strip()

    except Exception as e:
        return f"ERROR: {str(e)}"


def run():
    with open("data/curated/curated_mcq.json", encoding="utf-8") as f:
        data = json.load(f)

    prompt_template = load_prompt()
    results = []

    total = len(data)
    start_total = time.time()

    for i, item in enumerate(data):
        print(f"\n--- [{i+1}/{total}] Processing ---")

        question = item["question"]
        options = format_options(item["options"])

        prompt = prompt_template.replace("{question}", question)
        prompt = prompt.replace("{options}", options)

        start_q = time.time()

        phi = safe_call(ask_phi, prompt)
        mistral = safe_call(ask_mistral, prompt)
        llama = safe_call(ask_llama, prompt)

        end_q = time.time()
        tempo_q = end_q - start_q

        elapsed = end_q - start_total
        avg = elapsed / (i + 1)
        remaining = avg * (total - (i + 1))

        print(f"Tempo questão: {tempo_q:.2f}s")
        print(f"Médio: {avg:.2f}s | Restante: {remaining/60:.2f} min")

        results.append({
            "question": question,
            "options": item["options"],
            "correct": item["answer"],
            "phi": phi,
            "mistral": mistral,
            "llama": llama
        })

    os.makedirs("results", exist_ok=True)

    with open("results/mcq_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    total_time = time.time() - start_total
    print(f"\n✔ Finalizado em {total_time/60:.2f} minutos")


if __name__ == "__main__":
    run()