# post_to_linkedin.py
import os
import json
import requests
from datetime import datetime, timezone

LINKEDIN_CLIENT_ID = os.environ["LINKEDIN_CLIENT_ID"]
LINKEDIN_CLIENT_SECRET = os.environ["LINKEDIN_CLIENT_SECRET"]
LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")  # put initial token or leave empty if you store refresh token flow
LINKEDIN_REFRESH_TOKEN = os.environ.get("LINKEDIN_REFRESH_TOKEN")  # if you obtained a refresh token

def load_draft():
    with open("draft_post.json", "r", encoding="utf-8") as f:
        return json.load(f)["post"]

def refresh_access_token_if_needed():
    # If you have a refresh token flow configured, implement refresh here.
    # LinkedIn's exact refresh flow depends on app configuration.
    return os.environ.get("LINKEDIN_ACCESS_TOKEN")

def get_member_urn(token):
    # Get the authenticated user's URN
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get("https://api.linkedin.com/v2/me", headers=headers, timeout=20)
    r.raise_for_status()
    data = r.json()
    return data["id"]  # this is the member id

def post_text(token, author_urn, body_text):
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }
    payload = {
      "author": f"urn:li:person:{author_urn}",
      "lifecycleState": "PUBLISHED",
      "specificContent": {
        "com.linkedin.ugc.ShareContent": {
          "shareCommentary": {
            "text": body_text
          },
          "shareMediaCategory": "NONE"
        }
      },
      "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    r = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    token = refresh_access_token_if_needed()
    post = load_draft()
    body = f"{post.get('headline','')}\n\n{post.get('body','')}\n\nResources: {'; '.join(post.get('resources',[]))}\n\n{' '.join(post.get('hashtags',[]))}"
    author_id = get_member_urn(token)
    resp = post_text(token, author_id, body)
    print("Posted to LinkedIn:", resp)
