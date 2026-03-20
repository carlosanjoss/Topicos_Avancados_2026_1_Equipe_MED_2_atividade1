# Projeto de Avaliação de Modelos de Linguagem para Questões Médicas

### Parte de Carlos Eduardo E. M. P. Anjos

## Descrição

Este projeto tem como objetivo avaliar o desempenho de diferentes modelos de linguagem na resolução de questões médicas, incluindo questões de múltipla escolha e questões discursivas. A avaliação foi realizada utilizando métricas tradicionais e semânticas, permitindo uma análise mais robusta da qualidade das respostas geradas.

Os modelos avaliados foram:

* LLaMA
* Mistral
* Phi

---

## Estrutura do Projeto

```
TOPICOS_AVANCADOS_2026_1_EQUIPE_MED/
│
├── data/
│   ├── curated/
│   │   ├── curated_mcq.json
│   │   └── curated_open.json
│   │
│   └── raw/
│       ├── multiple_choice.json
│       ├── open_questions.jsonl
│       └── prova.pdf
│
├── prompts/
│   ├── mcq_prompt.txt
│   └── open_prompt.txt
│
├── results/
│   ├── mcq_metrics.json
│   ├── mcq_results.json
│   ├── open_metrics.json
│   └── open_results.json
│
├── src/
│   ├── models/
│   │   └── local.py
│   │
│   ├── curator_mcq.py
│   ├── curator_opq.py
│   ├── evaluation_mcq.py
│   ├── evaluation_open.py
│   ├── extract_pdf.py
│   ├── inference_mcq.py
│   ├── inference_opq.py
│   └── utils.py
│
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Curadoria dos Dados

A curadoria foi realizada manualmente, garantindo:

* Classificação de dificuldade
* Área médica
* Referência confiável

Os dados foram separados em:

* Questões de múltipla escolha (MCQ)
* Questões discursivas (Open Questions)

---

## Execução

### 1. Baixar o Ollama:

Baixe o Ollama diretamente no site

```
https://ollama.com/download
```

### 2. Instale os 3 modelos:

```
ollama pull llama3
ollama pull mistral
ollama pull phi3
```

### 3. Inicie o servidor:

```
ollama serve
```

### 4. Requerimentos:

Primeiro instale o ambiente virtual, logo após os requirements.txt:

```
pip install -r requirements.txt
```

### 5. Inferência

Para rodar os modelos nas questões:

```
python src/inference_mcq.py
python src/inference_opq.py
```

---

### 6. Avaliação

Para calcular as métricas:

```
python src/evaluate.py
```

---

## Resultados

Para as questões de múltipla escolha foi usado a métrica de acurácia , acurácia é a proporção de respostas corretas em relação ao total de questões. Para as questões
de resposta livre foram usados 5 métricas:

BLEU - mede o quanto o texto gerado coincide com um texto de referência com base na sobreposição de n-gramas, penalizando sequências muito curtas;

ROUGE - avalia a qualidade do texto gerado medindo o quanto ele cobre o conteúdo do texto de referência, também baseado em sobreposição de palavras ou n-gramas;

Similaridade Semântica - mede o quanto dois textos têm o mesmo significado, mesmo que usem palavras diferentes, geralmente usando embeddings;

F1 - é a média harmônica entre precisão e recall, equilibrando erros de falsos positivos e falsos negativos;

BERTScore - compara textos usando representações profundas de linguagem (BERT), avaliando similaridade semântica palavra por palavra com base em contexto;


### 🔹 Questões de Múltipla Escolha (Accuracy)

```
LLaMA   : 0.4660
Mistral : 0.3981
Phi     : 0.3395
```

O modelo LLaMA apresentou melhor desempenho em questões objetivas, indicando maior capacidade de selecionar alternativas corretas.

---

### 🔹 Questões Discursivas

```
LLaMA
- BLEU: 0.0817
- ROUGE: 0.1595
- Similaridade Semântica: 0.7811
- F1: 0.2462
- BERTScore: 0.7874

Mistral
- BLEU: 0.1158
- ROUGE: 0.1990
- Similaridade Semântica: 0.8069
- F1: 0.2941
- BERTScore: 0.8155

Phi
- BLEU: 0.0837
- ROUGE: 0.1638
- Similaridade Semântica: 0.7622
- F1: 0.2630
- BERTScore: 0.8015
```

---

## Análise dos Resultados

Nos resultados discursivos, o modelo Mistral apresentou desempenho superior em todas as métricas relevantes, especialmente nas métricas semânticas, indicando maior capacidade de compreender e gerar respostas alinhadas ao conteúdo esperado.

O modelo Phi apresentou desempenho intermediário, enquanto o LLaMA teve menor desempenho nesse tipo de tarefa.

Por outro lado, nas questões de múltipla escolha, o LLaMA obteve melhor desempenho, sugerindo maior eficácia em tarefas objetivas.

---

## Discussão

Os resultados evidenciam que:

* Métricas como BLEU e ROUGE possuem limitações para avaliação de respostas abertas
* Métricas semânticas (BERTScore e similaridade) são mais adequadas para esse tipo de tarefa
* Existe um trade-off entre desempenho em questões objetivas e discursivas



---

## Conclusão

O modelo Mistral demonstrou melhor desempenho em tarefas discursivas, sendo mais adequado para geração de respostas abertas em contexto médico. Já o LLaMA apresentou melhor desempenho em questões de múltipla escolha.

Os resultados reforçam a importância do uso de métricas semânticas na avaliação de modelos de linguagem em tarefas complexas.

---
