import fitz
import re
import json
from tqdm import tqdm

pdf_path = "data/raw/prova.pdf"

doc = fitz.open(pdf_path)

full_text = ""

for page in tqdm(doc):
    full_text += page.get_text()

pattern = r"Question\s+(\d+\.\d+).*?\((A)\).*?Correct Response:\s*([A-Z])"

questions = re.split(r"Question\s+\d+\.\d+", full_text)

results = []

for q in questions[1:]:

    question_match = re.search(r"^(.*?)\([A]\)", q, re.S)

    options = re.findall(r"\(([A-E])\)\s*(.*)", q)

    answer_match = re.search(r"Correct Response:\s*([A-Z])", q)

    explanation_match = re.search(r"OpenEvidence Explanation(.*?)References", q, re.S)

    references_match = re.findall(r"\d+\.\s*(.*)", q)

    if not question_match or not answer_match:
        continue

    options_dict = {}

    for opt in options:
        letter = opt[0]
        text = opt[1].strip()
        options_dict[letter] = text

    result = {
        "question": question_match.group(1).strip(),
        "options": options_dict,
        "answer": answer_match.group(1),
        "explanation": explanation_match.group(1).strip() if explanation_match else "",
        "references": references_match
    }

    results.append(result)

with open("data/raw/multiple_choice.json", "w") as f:
    json.dump(results, f, indent=2)

print("Questions extracted:", len(results))