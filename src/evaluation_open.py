import json
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
from utils import clean_text

from bert_score import score
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

embedder = SentenceTransformer('all-MiniLM-L6-v2')

smooth = SmoothingFunction().method1


def semantic_similarity(gold, pred):
    emb1 = embedder.encode([gold])
    emb2 = embedder.encode([pred])
    return cosine_similarity(emb1, emb2)[0][0]


def f1_score(gold, pred):
    gold_tokens = set(gold.split())
    pred_tokens = set(pred.split())

    common = gold_tokens & pred_tokens

    if len(common) == 0:
        return 0

    precision = len(common) / len(pred_tokens)
    recall = len(common) / len(gold_tokens)

    return 2 * (precision * recall) / (precision + recall)


def evaluate():
    with open("results/open_results.json", encoding="utf-8") as f:
        data = json.load(f)

    results = {
        "llama": [],
        "mistral": [],
        "phi": []
    }

    bert_inputs = {
        "llama": {"gold": [], "pred": []},
        "mistral": {"gold": [], "pred": []},
        "phi": {"gold": [], "pred": []}
    }

    for item in data:
        gold = clean_text(item["gold"])

        for model in ["llama", "mistral", "phi"]:
            pred = clean_text(item[model])

            bleu = sentence_bleu(
                [gold.split()],
                pred.split(),
                weights=(0.5, 0.5),
                smoothing_function=smooth
            )

            rouge = scorer.score(gold, pred)["rougeL"].fmeasure
            sim = semantic_similarity(gold, pred)
            f1 = f1_score(gold, pred)

            results[model].append({
                "bleu": bleu,
                "rouge": rouge,
                "semantic": sim,
                "f1": f1
            })

            bert_inputs[model]["gold"].append(gold)
            bert_inputs[model]["pred"].append(pred)

    final = {}

    for model in results:
        bleu_avg = sum(x["bleu"] for x in results[model]) / len(results[model])
        rouge_avg = sum(x["rouge"] for x in results[model]) / len(results[model])
        sim_avg = sum(x["semantic"] for x in results[model]) / len(results[model])
        f1_avg = sum(x["f1"] for x in results[model]) / len(results[model])

        P, R, F1 = score(
            bert_inputs[model]["pred"],
            bert_inputs[model]["gold"],
            model_type="distilbert-base-uncased",
            verbose=False
        )

        bert_avg = float(F1.mean())

        final[model] = {
            "bleu": float(bleu_avg),
            "rouge": float(rouge_avg),
            "semantic_similarity": float(sim_avg),
            "f1": float(f1_avg),
            "bertscore": float(bert_avg)
            }

    print("\nRESULTADOS FINAIS:")
    for model in final:
        print(f"\n{model.upper()}")
        for metric, value in final[model].items():
            print(f"{metric}: {value:.4f}")

    with open("results/open_metrics.json", "w", encoding="utf-8") as f:
        json.dump(final, f, indent=2)


if __name__ == "__main__":
    evaluate()