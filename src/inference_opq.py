import os
import json
import time
from models.local import ask_llama, ask_mistral, ask_phi


def load_prompt():
    with open("prompts/open_prompt.txt", encoding="utf-8") as f:
        return f.read()


def safe_call(fn, prompt):
    try:
        response = fn(prompt)

        if isinstance(response, str) and "error" in response.lower():
            return f"ERROR: {response}"

        return response
    except Exception as e:
        return f"ERROR: {str(e)}"


def run():
    with open("data/curated/curated_open.json", encoding="utf-8") as f:
        data = json.load(f)

    prompt_template = load_prompt()

    results = []

    total = len(data)
    start_total = time.time()

    for i, item in enumerate(data):
        print(f"\n--- [{i+1}/{total}] Processando ---")

        question = item["question"]
        prompt = prompt_template.replace("{question}", question)

        start = time.time()

        llama = safe_call(ask_llama, prompt)
        mistral = safe_call(ask_mistral, prompt)
        phi = safe_call(ask_phi, prompt)

        end = time.time()

        tempo_questao = end - start

        elapsed = end - start_total
        avg = elapsed / (i + 1)
        remaining = avg * (total - (i + 1))

        print(f"Tempo questão: {tempo_questao:.2f}s")
        print(f"Tempo médio: {avg:.2f}s")
        print(f"Tempo restante estimado: {remaining/60:.2f} min")

        results.append({
            "question": question,
            "gold": item["gold_answer"],
            "llama": llama,
            "mistral": mistral,
            "phi": phi,
            "time": round(tempo_questao, 2)
        })

    os.makedirs("results", exist_ok=True)

    with open("results/open_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    total_time = time.time() - start_total
    print(f"\nTempo total: {total_time/60:.2f} minutos")


if __name__ == "__main__":
    run()