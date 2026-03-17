import json

def classify(question):
    q = question.lower()

    if "cholesterol" in q or "heart" in q:
        area = "cardiology"
    elif "brain" in q:
        area = "neurology"
    elif "infection" in q or "virus" in q:
        area = "infectious_disease"
    elif "hormone" in q:
        area = "endocrinology"
    elif "lung" in q:
        area = "pulmonology"
    elif "psych" in q:
        area = "psychiatry"
    else:
        area = "general_medicine"

    size = len(question)

    if size < 120:
        difficulty = "easy"
    elif size < 250:
        difficulty = "medium"
    else:
        difficulty = "hard"

    reference = "UpToDate"

    return difficulty, area, reference


def curate_mcq():
    with open("data/raw/multiple_choice.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    curated = []

    for item in data:
        difficulty, area, reference = classify(item["question"])

        curated.append({
            **item,
            "difficulty": difficulty,
            "area": area,
            "reference": reference
        })

    with open("data/curated/curated_mcq.json", "w", encoding="utf-8") as f:
        json.dump(curated, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    curate_mcq()