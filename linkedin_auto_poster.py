import os
import json
import requests
from datetime import datetime

# Configuration from environment variables
LINKEDIN_ACCESS_TOKEN = os.environ.get('LINKEDIN_ACCESS_TOKEN')
LINKEDIN_PERSON_URN = os.environ.get('LINKEDIN_PERSON_URN')
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

def generate_post_content():
    """Generate LinkedIn post content using Groq (free tier)"""
    
    prompt = f"""Generate a professional LinkedIn post about data science, machine learning, or AI.
    
    Requirements:
    - 150-250 words
    - Include relevant hashtags (3-5 hashtags)
    - Make it engaging and informative
    - Focus on: trends, tips, insights, or interesting facts
    - Today's date: {datetime.now().strftime('%B %d, %Y')}
    - Vary topics: ML algorithms, data visualization, AI ethics, career tips, tools, best practices, etc.
    - Write in a professional but conversational tone
    
    Return only the post text, ready to publish. No extra commentary."""
    
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    response = requests.post(
        'https://api.groq.com/openai/v1/chat/completions',
        headers=headers,
        json=data,
        timeout=30
    )
    
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        raise Exception(f"Groq API error: {response.status_code} - {response.text}")

def get_person_urn():
    """Get LinkedIn person URN (user ID) - tries multiple methods"""
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    # Try method 1: OpenID Connect
    try:
        response = requests.get('https://api.linkedin.com/v2/userinfo', headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('sub')
    except:
        pass
    
    # Try method 2: Legacy /me endpoint
    try:
        response = requests.get('https://api.linkedin.com/v2/me', headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get('id')
    except:
        pass
    
    raise Exception("Failed to get Person URN from LinkedIn API")

def post_to_linkedin(content):
    """Post content to LinkedIn"""
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    
    # Get person URN - either from env var or fetch it
    person_urn = LINKEDIN_PERSON_URN
    if not person_urn or person_urn == "":
        print("Person URN not provided, fetching automatically...")
        person_urn = get_person_urn()
        print(f"Fetched Person URN: {person_urn}")
    
    post_data = {
        "author": f"urn:li:person:{person_urn}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    response = requests.post(
        'https://api.linkedin.com/v2/ugcPosts',
        headers=headers,
        json=post_data
    )
    
    return response

def save_post_record(content, status):
    """Save posted content to track history"""
    record = {
        'timestamp': datetime.now().isoformat(),
        'content': content,
        'status': status
    }
    
    # Append to posts.json file
    try:
        with open('posts.json', 'r') as f:
            posts = json.load(f)
    except FileNotFoundError:
        posts = []
    
    posts.append(record)
    
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

def main():
    try:
        # Generate content
        print("Generating post content...")
        content = generate_post_content()
        print(f"Generated content:\n{content}\n")
        
        # Post to LinkedIn
        print("Posting to LinkedIn...")
        response = post_to_linkedin(content)
        
        if response.status_code == 201:
            print("✅ Successfully posted to LinkedIn!")
            save_post_record(content, 'success')
        else:
            print(f"❌ Failed to post: {response.status_code}")
            print(f"Response: {response.text}")
            save_post_record(content, f'failed: {response.status_code}')
            exit(1)
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        save_post_record("", f'error: {str(e)}')
        exit(1)

if __name__ == "__main__":
    main()
