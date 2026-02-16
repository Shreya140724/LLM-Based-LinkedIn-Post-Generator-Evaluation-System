# 🚀 AI LinkedIn Post Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-green)
![VectorDB](https://img.shields.io/badge/VectorDB-FAISS-orange)
![LLM](https://img.shields.io/badge/LLM-Ollama-purple)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![Architecture](https://img.shields.io/badge/Architecture-RAG-brightgreen)
![Mode](https://img.shields.io/badge/Mode-Offline-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

------------------------------------------------------------------------

## 📌 Overview

AI-powered LinkedIn Post Generator built using **LangChain + Ollama
(Offline LLM)** with a customizable **Streamlit UI**.

This application allows users to generate professional LinkedIn posts
with:

-   Tone control\
-   Creativity tuning\
-   Hook-line generation\
-   Format selection (Paragraph / Bullet Points)\
-   AI-based post scoring\
-   Analytics & insights

The system demonstrates structured prompt engineering, output
validation, and multi-stage LLM pipelines.

------------------------------------------------------------------------

## 📑 Table of Contents

-   [Features](#-features)
-   [Architecture](#-architecture)
-   [Project Structure](#-project-structure)
-   [Installation](#-installation)
-   [Usage](#-usage)
-   [Configuration](#-configuration)
-   [Analytics & Scoring](#-analytics--scoring)
-   [Future Improvements](#-future-improvements)
-   [Author](#-author)

------------------------------------------------------------------------

## ✨ Features

### 🎨 Content Customization

-   Topic dropdown + custom topic input
-   Length control (Short / Medium / Long)
-   Tone selection
-   Emoji control
-   Call-to-action selection
-   Paragraph or Bullet point formatting
-   Strong hook toggle

### 🎛 Creativity Control

User-controlled creativity level mapped to model temperature: - **Low**
-- Structured & Deterministic\
- **Balanced** -- Moderate creativity\
- **High** -- Creative & Diverse

### 📊 Analytics & Insights

After generation: - Word count - Character count - Estimated reading
time - Hashtag count

### 🧠 AI Post Scoring System

Second-stage LLM evaluation scores the post on: - Engagement - Clarity -
Hook Strength - CTA Strength

Structured JSON output parsing is used for scoring.

### 🔁 Regenerate Support

Generate alternative versions with the same input parameters.

------------------------------------------------------------------------

## 🏗 Architecture

    User Input
        ↓
    Streamlit UI
        ↓
    Prompt Builder
        ↓
    Ollama LLM (Offline)
        ↓
    Post Processor
        ↓
    Analytics + AI Scoring
        ↓
    Final Output

### Key Concepts Demonstrated

-   Prompt Engineering\
-   Controlled LLM Generation\
-   Structured JSON Parsing\
-   Regex-based Post-processing\
-   Two-stage LLM Pipeline (Generation + Evaluation)

------------------------------------------------------------------------

## 📂 Project Structure

    POST_GENERATION/
    │
    ├── data/
    │   └── processed_posts.json
    ├── few_shot.py
    ├── llm_helper.py
    ├── main.py
    ├── post_generator.py
    ├── preprocess.py
    ├── .env
    └── README.md

### 📄 File Descriptions

  --------------------------------------------------------------------------
  File                          Purpose
  ----------------------------- --------------------------------------------
  `main.py`                     Streamlit UI & app logic

  `post_generator.py`           Prompt building, generation, analytics &
                                scoring

  `llm_helper.py`               LLM initialization (Ollama / Groq)

  `few_shot.py`                 Few-shot post filtering & tag management

  `preprocess.py`               Metadata extraction & dataset preparation

  `data/processed_posts.json`   Structured example posts
  --------------------------------------------------------------------------

------------------------------------------------------------------------

## ⚙ Installation

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/Shreya140724/LLM-Based-LinkedIn-Post-Generator-Evaluation-System.git
cd POST_GENERATION
```

### 2️⃣ Create Virtual Environment

Using Conda:

``` bash
conda create -n postgen python=3.10
conda activate postgen
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit App

``` bash
streamlit run main.py
```

------------------------------------------------------------------------

## ▶ Usage

1.  Select or enter a topic.
2.  Choose tone, length, and creativity level.
3.  Toggle hook, emojis, and CTA.
4.  Generate post.
5.  Review analytics and AI scoring.
6.  Regenerate if needed.

------------------------------------------------------------------------

## 🔧 Configuration

-   Modify `.env` file to configure model providers.
-   Adjust temperature mapping inside `post_generator.py`.
-   Update few-shot examples in `processed_posts.json` for better
    personalization.

------------------------------------------------------------------------

## 📊 Analytics & Scoring

The system performs:

-   Text analytics (word count, character count, reading time)
-   Hashtag detection
-   AI-based evaluation via structured JSON parsing

This ensures both **content quality** and **engagement optimization**.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   A/B post generation comparison\
-   Trending hashtag extraction via API\
-   Deployment on Streamlit Cloud\
-   User post history logging\
-   Advanced sentiment scoring

------------------------------------------------------------------------

## 👩‍💻 Author

**Shreya Sidabache**\
AI / ML Engineer

------------------------------------------------------------------------

## 📜 License

This project is intended for educational and portfolio purposes.
