import json
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer
from utils import clean_text

scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

def evaluate():
    with open("results/open_results.json", encoding="utf-8") as f:
        data = json.load(f)

    results = {
        "llama": [],
        "mistral": [],
        "phi": []
    }

    for item in data:
        gold = clean_text(item["gold"])

        for model in ["llama", "mistral", "phi"]:
            pred = clean_text(item[model])

            bleu = sentence_bleu([gold.split()], pred.split())
            rouge = scorer.score(gold, pred)["rougeL"].fmeasure

            results[model].append({
                "bleu": bleu,
                "rouge": rouge
            })

    # média
    final = {}

    for model in results:
        bleu_avg = sum(x["bleu"] for x in results[model]) / len(results[model])
        rouge_avg = sum(x["rouge"] for x in results[model]) / len(results[model])

        final[model] = {
            "bleu": bleu_avg,
            "rouge": rouge_avg
        }

    print(final)

    with open("results/open_metrics.json", "w") as f:
        json.dump(final, f, indent=2)


if __name__ == "__main__":
    evaluate()