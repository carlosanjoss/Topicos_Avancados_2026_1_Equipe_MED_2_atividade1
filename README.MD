# 🧠 Curadoria de Datasets e Inferência com LLMs (Domínio Médico)

## 📌 Descrição do Projeto

Este projeto foi desenvolvido como parte da atividade avaliativa da disciplina de Tópicos Avançados, com foco na **curadoria de datasets médicos** e na **avaliação de modelos de linguagem (LLMs)** em tarefas de inferência.

O objetivo principal é analisar o desempenho de diferentes modelos em dois tipos de tarefas:

* **Questões discursivas (open-ended)**
* **Questões de múltipla escolha (MCQ)**

---

## 🎯 Objetivos

* Realizar a **curadoria manual e assistida** dos dados
* Aplicar **modelos de linguagem locais (LLMs)** para inferência
* Comparar o desempenho dos modelos utilizando **métricas quantitativas**
* Avaliar diferenças de desempenho entre tarefas objetivas e discursivas

---

## 🗂️ Estrutura do Projeto

```
Topicos_Avancados_2026-1_Equipe_MED_2_atividade1

├── data/
│   ├── raw/
│   ├── curated/
│
├── src/
│   ├── models/
│   │   └── local.py
│   ├── curator_mcq.py
│   ├── curator_open.py
│   ├── inference_open.py
│   ├── inference_mcq.py
│   ├── evaluation_open.py
│   ├── evaluation_mcq.py
│   └── utils.py
│
├── results/
│   ├── open_results.json
│   ├── mcq_results.json
│   ├── open_metrics.json
│   └── mcq_metrics.json
│
├── prompts/
└── README.md
```

---

## 🧪 Modelos Utilizados

Os modelos foram executados localmente utilizando o **Ollama**, garantindo independência de APIs externas:

* `llama3`
* `mistral`
* `phi3`

---

## ⚙️ Como Executar o Projeto

### 1. Instalar o Ollama

```
https://ollama.com/download
```

---

### 2. Baixar os modelos

```bash
ollama pull llama3
ollama pull mistral
ollama pull phi3
```

---

### 3. Executar o servidor local

```bash
ollama serve
```

---

### 4. Rodar a curadoria

```bash
python src/curator_mcq.py
python src/curator_open.py
```

---

### 5. Executar inferência

```bash
python src/inference_open.py
python src/inference_mcq.py
```

---

### 6. Avaliar resultados

```bash
python src/evaluation_open.py
python src/evaluation_mcq.py
```

---

## 📊 Métricas Utilizadas

### 🔹 Questões Discursivas

* **BLEU** → Similaridade textual
* **ROUGE-L** → Sobreposição semântica

### 🔹 Questões Objetivas

* **Acurácia** → Proporção de respostas corretas

---

## 📈 Resultados Obtidos

### ✔️ Acurácia (MCQ)

* LLaMA: **46.6%**
* Mistral: **39.8%**
* Phi: **33.9%**

---

### ✔️ Métricas Discursivas

| Modelo  | BLEU  | ROUGE |
| ------- | ----- | ----- |
| LLaMA   | 0.015 | 0.159 |
| Mistral | 0.021 | 0.199 |
| Phi     | 0.010 | 0.163 |

---

## 🧠 Análise dos Resultados

* O modelo **LLaMA apresentou melhor desempenho em tarefas objetivas**, indicando maior capacidade de seleção correta de alternativas.
* O modelo **Mistral apresentou melhor desempenho em tarefas discursivas**, com maior sobreposição semântica (ROUGE).
* O modelo **Phi apresentou desempenho inferior em ambos os cenários**.

Observa-se que o desempenho dos modelos varia de acordo com o tipo de tarefa, evidenciando que **não existe um modelo universalmente superior**, mas sim modelos mais adequados para contextos específicos.

---

## ⚠️ Considerações Importantes

* Valores baixos de BLEU são esperados, pois modelos de linguagem tendem a **parafrasear respostas**, em vez de reproduzir literalmente o texto.
* O uso de modelos locais garante:

  * Reprodutibilidade
  * Independência de APIs pagas
  * Execução offline

---

## 👥 Equipe

* Carlos

---

## 🎥 Vídeo Demonstrativo

(Adicionar link aqui)

---

## 📄 Tutorial em PDF

(Adicionar link ou anexar conforme solicitado)

---

## ✅ Conclusão

O projeto demonstrou, na prática, o comportamento de diferentes LLMs em tarefas médicas, evidenciando:

* Diferenças entre **raciocínio objetivo e geração textual**
* Limitações de métricas tradicionais em avaliação de linguagem
* Importância da escolha do modelo conforme a tarefa

---

## 🚀 Tecnologias Utilizadas

* Python
* Ollama
* NLTK
* Rouge-score
* JSON

---

## 📌 Reprodutibilidade

Todo o projeto pode ser reproduzido seguindo as etapas descritas neste README.

---
