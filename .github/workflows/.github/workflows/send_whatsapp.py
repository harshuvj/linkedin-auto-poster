# send_whatsapp.py
import os
import json
import requests

WHATSAPP_TOKEN = os.environ["WHATSAPP_TOKEN"]           # from Meta developer console
WHATSAPP_PHONE_ID = os.environ["WHATSAPP_PHONE_ID"]     # phone id (the 'from' id)
WHATSAPP_TO_NUMBER = os.environ["WHATSAPP_TO_NUMBER"]   # your personal number in E.164 format

def load_draft():
    with open("draft_post.json", "r", encoding="utf-8") as f:
        return json.load(f)["post"]

def format_message(post):
    headline = post.get("headline","").strip()
    body = post.get("body","").strip()
    resources = post.get("resources",[])
    hashtags = " ".join(post.get("hashtags",[]))
    resources_text = "\n".join([f"- {r}" for r in resources]) if resources else ""
    message = f"*{headline}*\n\n{body}\n\nResources:\n{resources_text}\n\n{hashtags}\n\nReply with *APPROVE* within 30 minutes to post this at 14:00 IST. If no approve, this draft will be skipped today."
    return message

def send_whatsapp_message(message):
    url = f"https://graph.facebook.com/v16.0/{WHATSAPP_PHONE_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
    payload = {
        "messaging_product": "whatsapp",
        "to": WHATSAPP_TO_NUMBER,
        "type": "text",
        "text": {"body": message}
    }
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    post = load_draft()
    msg = format_message(post)
    resp = send_whatsapp_message(msg)
    print("WhatsApp sent:", resp)
