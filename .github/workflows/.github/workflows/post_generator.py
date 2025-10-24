# post_generator.py
import os, json, requests
from datetime import datetime, timezone

HF_TOKEN = os.environ["HF_TOKEN"]
HF_MODEL = os.environ.get("HF_MODEL", "gpt2")  # change to a better HF model if available

# Replace the text below with the full system prompt we finalized (I'll paste it below).
SYSTEM_PROMPT = """
You are an experienced Senior Analytics & AI Leader in financial services and enterprise transformation.
Your style is corporate/consulting. Produce a LinkedIn post in short paragraphs with business outcomes.
Rules:
- Always include resources (1-2 links) and 5-8 relevant hashtags.
- Rotate formats: Insights, Breaking news, Tutorial, Opinion.
- Use BFSI examples >= 60% of posts; occasionally reference retail/healthcare/manufacturing.
- Output JSON: headline, body, resources(list), hashtags(list), theme, index
"""

WEEKDAY_THEMES = {
    "Monday":"Machine Learning Monday",
    "Tuesday":"Tech/Tactic Tuesday",
    "Wednesday":"Wednesday: Analytics Spotlight",
    "Thursday":"Thoughtful Thursday (AI Strategy)",
    "Friday":"Feature Friday (Case Studies)",
    "Saturday":"Skillup Saturday (Tutorials)",
    "Sunday":"Strategy Sunday (Opinion & Trends)"
}

def load_counters():
    with open("counters.json","r",encoding="utf-8") as f:
        return json.load(f)

def call_hf(prompt):
    url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 500}}
    r = requests.post(url, headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    out = r.json()
    # try common response shapes
    if isinstance(out, list):
        # some HF models return [{"generated_text":"..."}]
        if len(out)>0 and isinstance(out[0], dict) and 'generated_text' in out[0]:
            return out[0]['generated_text']
        return out[0].get('generated_text', str(out))
    if isinstance(out, dict) and 'generated_text' in out:
        return out['generated_text']
    if isinstance(out, str):
        return out
    return json.dumps(out)

def generate_post_json(theme_name, index):
    # Compose a short instruction for HF and ask for JSON output
    today = datetime.now(timezone.utc).date().isoformat()
    instruction = f"""{SYSTEM_PROMPT}

Generate ONE LinkedIn post for date {today}.
Theme: {theme_name}
ThemeIndex: {index}
Output JSON only with these fields:
- headline (string)
- body (string; 3 short paragraphs max)
- resources (array of 1-2 links)
- hashtags (array of 5-8 hashtags)
Do not include extra fields.
"""
    out = call_hf(instruction)
    # Try to parse JSON; if cannot, package fallback
    try:
        parsed = json.loads(out)
        return parsed
    except Exception:
        # fallback: simple split
        lines = out.strip().splitlines()
        headline = lines[0] if lines else theme_name
        body = "\n".join(lines[1:6]) if len(lines)>1 else ""
        return {
            "headline": f"{theme_name} — {headline}",
            "body": body,
            "resources": [],
            "hashtags": ["#DataScience","#MachineLearning","#AI","#Analytics"]
        }

if __name__ == "__main__":
    # Determine today's weekday & theme & get index from counters
    counters = load_counters()
    today_weekday = datetime.now().strftime("%A")  # e.g., "Monday"
    theme = WEEKDAY_THEMES.get(today_weekday, f"{today_weekday} Post")
    # note: index shown to user equals counters[weekday] + 1 (next potential index)
    next_index = counters.get(today_weekday, 0) + 1

    post = generate_post_json(theme, next_index)
    # Add metadata so approval & posting jobs know theme & index
    artifact = {
        "meta": {
            "weekday": today_weekday,
            "theme": theme,
            "index": next_index,
            "generated_utc": datetime.now(timezone.utc).isoformat()
        },
        "post": post
    }
    with open("draft_post.json","w",encoding="utf-8") as f:
        json.dump(artifact, f, ensure_ascii=False, indent=2)
    print("Draft generated and saved to draft_post.json")
