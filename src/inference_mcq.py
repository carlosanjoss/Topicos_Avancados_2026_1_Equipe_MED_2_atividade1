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


def load_existing_results(path):
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()

            if not content:
                print("⚠️ Arquivo vazio → reiniciando")
                return []

            return json.loads(content)

    except Exception as e:
        print(f"⚠️ Arquivo corrompido → resetando: {e}")
        return []


def save_results(path, results):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


def run():
    input_path = "data/curated/curated_mcq.json"
    output_path = "results/mcq_results.json"

    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    prompt_template = load_prompt()

    results = load_existing_results(output_path)

    print(f"🔁 Itens já processados: {len(results)}")

    processed = set()
    for r in results:
        if isinstance(r, dict) and "question" in r:
            processed.add(r["question"])

    total = len(data)
    start_total = time.time()

    for i, item in enumerate(data):

        question = item.get("question")

        if not question:
            print(f"⚠️ Questão inválida no índice {i}")
            continue

        if question in processed:
            print(f"[SKIP] {question[:60]}...")
            continue

        print(f"\n--- [{len(results)+1}/{total}] Processing ---")

        if "options" not in item:
            print("❌ Sem options → pulando")
            continue

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

        avg = elapsed / (len(results) + 1)
        remaining = avg * (total - (len(results) + 1))

        print(f"Tempo questão: {tempo_q:.2f}s")
        print(f"Médio: {avg:.2f}s | Restante: {remaining/60:.2f} min")

        result_item = {
            "question": question,
            "options": item["options"],
            "correct": item.get("answer"),
            "phi": phi,
            "mistral": mistral,
            "llama": llama
        }

        results.append(result_item)
        processed.add(question)

        save_results(output_path, results)

        print(f"💾 Salvo ({len(results)}/{total})")

    total_time = time.time() - start_total
    print(f"\n✔ Finalizado em {total_time/60:.2f} minutos")


if __name__ == "__main__":
    run()