import json

def classify(question):
    q = question.lower()

    if "infection" in q or "virus" in q:
        area = "infectious_disease"
    elif "heart" in q:
        area = "cardiology"
    elif "brain" in q:
        area = "neurology"
    elif "diabetes" in q:
        area = "endocrinology"
    else:
        area = "general_medicine"

    size = len(question)

    if size < 120:
        difficulty = "easy"
    elif size < 250:
        difficulty = "medium"
    else:
        difficulty = "hard"

    reference = "PubMed review"

    return difficulty, area, reference


def curate_open():
    curated = []

    with open("data/raw/open_questions.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)

            question = item["Question"]

            difficulty, area, reference = classify(question)

            curated.append({
                "question": question,
                "gold_answer": item["Free_form_answer"],
                "must_have": item["Must_have"],
                "nice_to_have": item["Nice_to_have"],
                "icd": item["ICD_10_diag"],
                "difficulty": difficulty,
                "area": area,
                "reference": reference
            })

    with open("results/open_results.json", "w", encoding="utf-8") as f:
        json.dump(curated, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    curate_open()