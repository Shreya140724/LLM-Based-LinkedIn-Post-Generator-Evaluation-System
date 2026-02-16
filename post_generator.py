from llm_helper import llm
import re
import json

# ---------------- LENGTH CONTROL ---------------- #

def get_length_str(length):
    if length == "Short":
        return "Exactly 2 to 3 short lines only."
    if length == "Medium":
        return "Exactly 5 to 7 lines."
    if length == "Long":
        return "At least 10 to 14 lines."


def enforce_length(post, length):
    lines = post.strip().split("\n")
    lines = [line for line in lines if line.strip() != ""]

    if length == "Short":
        return "\n".join(lines[:3])
    if length == "Medium":
        return "\n".join(lines[:7])
    if length == "Long":
        return "\n".join(lines[:14])

    return post


def clean_numbering(post):
    cleaned_lines = []
    for line in post.split("\n"):
        cleaned_line = re.sub(r"^\s*\d+\.\s*", "", line)
        cleaned_lines.append(cleaned_line)
    return "\n".join(cleaned_lines)


# ---------------- ANALYTICS ---------------- #

def get_analytics(post):
    words = post.split()
    word_count = len(words)
    char_count = len(post)
    reading_time = round(word_count / 200, 2)
    hashtag_count = len([w for w in words if w.startswith("#")])

    return {
        "Word Count": word_count,
        "Character Count": char_count,
        "Estimated Reading Time (mins)": reading_time,
        "Hashtag Count": hashtag_count
    }


# ---------------- SCORING ---------------- #

def score_post(post):
    scoring_prompt = f"""
You are a LinkedIn content evaluator.

Score the following post out of 10 for:
- Engagement
- Clarity
- Hook Strength
- CTA Strength

Return strictly in JSON format:
{{
  "Engagement": 8,
  "Clarity": 9,
  "Hook Strength": 7,
  "CTA Strength": 8
}}

Post:
{post}
"""

    response = llm.invoke(scoring_prompt)

    try:
        scores = json.loads(response.content)
    except:
        scores = {"Error": "Scoring failed"}

    return scores


# ---------------- MAIN GENERATOR ---------------- #

def generate_post(length, language, tag, tone, emoji_style, cta,
                  creativity_level, add_hook, post_format):

    length_instruction = get_length_str(length)

    # Map creativity level to temperature
    temperature_map = {
        "Low": 0.2,
        "Balanced": 0.5,
        "High": 0.8
    }

    llm.temperature = temperature_map[creativity_level]

    if language == "Hinglish":
        language_instruction = """
Write in Hinglish using English alphabet.
Mix Hindi and English naturally.
"""
    else:
        language_instruction = "Write in professional English only."

    hook_instruction = ""
    if add_hook:
        hook_instruction = "Start with a strong attention-grabbing hook line."

    if post_format == "Bullet Points":
        format_instruction = """
Use bullet points.
Use '-' only.
Do not number points.
"""
    else:
        format_instruction = """
Write in paragraph format.
Do not use bullet points.
Do not number lines.
"""

    prompt = f"""
Generate a LinkedIn post.

Topic: {tag}
Tone: {tone}
Emoji Style: {emoji_style}
Call To Action: {cta}

Length Rule: {length_instruction}
{hook_instruction}
{language_instruction}
{format_instruction}

Add relevant hashtags at the end.
"""

    response = llm.invoke(prompt)
    content = response.content

    content = enforce_length(content, length)
    content = clean_numbering(content)

    return content
