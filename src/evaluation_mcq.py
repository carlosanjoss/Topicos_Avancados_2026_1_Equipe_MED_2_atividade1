import json
import re

def extract_letter(text):
    match = re.search(r'[A-E]', text.upper())
    return match.group(0) if match else None

def evaluate():
    with open("results/mcq_results.json", encoding="utf-8") as f:
        data = json.load(f)

    scores = {
        "llama": 0,
        "mistral": 0,
        "phi": 0
    }

    total = len(data)

    for item in data:
        correct = item["correct"]

        for model in scores:
            pred = extract_letter(item[model])

            if pred == correct:
                scores[model] += 1

    for model in scores:
        scores[model] = scores[model] / total

    print(scores)

    with open("results/mcq_metrics.json", "w") as f:
        json.dump(scores, f, indent=2)


if __name__ == "__main__":
    evaluate()