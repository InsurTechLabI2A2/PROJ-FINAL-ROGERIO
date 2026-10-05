# InsurMinds — Comparador Inteligente de Apólices D&O 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit%20%7C%20Pydantic%20%7C%20OpenAI%2FAnthropic-green.svg)]()

> **Projeto Final de Graduação — Instituto de Inteligência Artificial Aplicada (I2A2)**  
> **Grupo:** InsurTechLab  
> **Tema:** Leitura, Extração, Estruturação e Comparação Inteligente de Apólices D&O (*Directors and Officers*) utilizando Inteligência Artificial Generativa e Agentes Especiais.

---

## 👥 Integrantes do Grupo (InsurTechLab)

* **Edmar Martelato**
* **Marisa De Moraes**
* **Roberto da Silva Goncalves**
* **Rogério Walmor Cervi**

---

## 📌 Visão Geral do Projeto

A comparação manual de apólices de seguro D&O é um processo altamente técnico e moroso, que exige a análise detalhada de dezenas de páginas contendo cláusulas jurídicas, limites de cobertura, sublimites, franquias, exclusões e extensões de garantia.

O **InsurMinds** é uma plataforma MVP desenvolvida para automatizar e otimizar essa análise através de uma **Arquitetura Orientada a Agentes Inteligentes** e **IA Generativa**. O sistema extrai e padroniza dados brutos em um esquema JSON estritamente tipado (via Pydantic) e realiza comparações campo a campo (*gap analysis*), gerando relatórios executivos instantâneos para tomada de decisão.

---

## 🛠️ Funcionalidades Principais

* 📄 **Ingestão Multi-formato:** Suporte à leitura de apólices e propostas em PDF e Imagens (com suporte a OCR).
* 🔍 **Extração Automática:** Captura estruturada de tomador, seguradora, limite máximo de garantia (LMG), franquias, retroatividade, coberturas e exclusões.
* 🏷️ **Validação de Schema (Pydantic/JSON Schema):** Garantia de dados limpos e padronizados no formato `schemas_policy.py`.
* ⚖️ **Comparativo Inteligente:** Agente comparador (`comparison_agent.py`) que realiza análise diferencial entre duas ou mais apólices, destacando vantagens, desvantagens e cláusulas críticas.
* 🖥️ **Interface Web Interativa (Streamlit):** Painel amigável (`app.py`) para upload de documentos, visualização do JSON e exportação de relatórios comparativos.

---

## 🏛️ Arquitetura do Sistema

O fluxo do **InsurMinds** é composto por agentes especializados trabalhando de forma sequencial e modular:

```text
[ Documentos PDF / Imagem ]
            │
            ▼
┌─────────────────────────┐
│   Agente de Recepção    │ (Validação de formato e preprocessamento OCR)
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Agente de Extração    │ (LLM Generativa + EXTRACTION_PROMPT.py)
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Agente de Validação    │ (Estruturação e Schema via schemas_policy.py)
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Agente Comparador      │ (Análise diferencial via comparison_agent.py)
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Relatório & Dashboard  │ (Exibição web em app.py e exportação)
└─────────────────────────┘
```

---

## 📁 Estrutura do Repositório

```text
PROJ-FINAL-ROGERIO/
├── README.md                                     # Documentação principal do projeto
├── LICENSE                                       # Licença MIT de código aberto
├── requirements.txt                              # Dependências Python do projeto
├── .env.example                                  # Modelo de variáveis de ambiente
├── app.py                                        # Interface Web interativa (Streamlit)
├── EXTRACTION_PROMPT.py                          # Prompts otimizados para extração de apólices D&O
├── schemas_policy.py                             # Definição dos Schemas Pydantic / JSON
├── comparison_agent.py                           # Agente comparador e gerador de insights
├── bash.sh                                       # Script auxiliar de execução/teste
├── Arquitetura de Agentes para Apólices D&O.json  # Especificação da arquitetura multi-agente
│
└── Projeto_Final_Artefatos/                      # Pasta Obrigatória de Artefatos (Edital I2A2)
    ├── InsurMinds_Projeto_Final.pptx             # Pitch Deck da Apresentação
    ├── InsurMinds_Projeto_Final.pdf              # Relatório Técnico completo em PDF
    ├── InsurMinds_Projeto_Final.mp4              # Vídeo demonstrativo (Link / Arquivo)
    └── README_ARTEFATOS.md                       # Detalhamento e links dos artefatos
```

---

## 🚀 Guia de Instalação e Execução

### 1. Pré-requisitos
* Python 3.11 ou superior instalado.
* Chave de API de LLM (OpenAI, Anthropic ou Google Gemini).

### 2. Clonar o Repositório
```bash
git clone https://github.com/InsurTechLabI2A2/PROJ-FINAL-ROGERIO.git
cd PROJ-FINAL-ROGERIO
```

### 3. Configurar o Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 4. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 5. Configurar as Variáveis de Ambiente
Crie um arquivo `.env` baseado no `.env.example`:
```bash
cp .env.example .env
```
Edite o arquivo `.env` e insira sua chave de API:
```env
OPENAI_API_KEY=sua_chave_aqui
# ou
ANTHROPIC_API_KEY=sua_chave_aqui
```

### 6. Executar a Aplicação Web (Streamlit)
```bash
streamlit run app.py
```
Acesse a aplicação no seu navegador em `http://localhost:8501`.

---

## 📂 Artefatos de Entrega Final

Todos os artefatos obrigatórios exigidos pelo Instituto I2A2 estão disponíveis na pasta [`Projeto_Final_Artefatos/`](./Projeto_Final_Artefatos/):

1. **Apresentação (Pitch Deck):** `Projeto_Final_Artefatos/InsurMinds_Projeto_Final.pptx`
2. **Relatório Técnico (PDF):** `Projeto_Final_Artefatos/InsurMinds_Projeto_Final.pdf`
3. **Vídeo Demonstrativo:** `Projeto_Final_Artefatos/InsurMinds_Projeto_Final.mp4`

---

## ⚖️ Licença

Este projeto é disponibilizado sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
